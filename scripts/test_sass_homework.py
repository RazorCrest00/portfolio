#!/usr/bin/env python3
"""Validate actual submission cells, saved HTML, rubric structure and download bundle.
Run with: venv/bin/python3 scripts/test_sass_homework.py
Browser behavior is checked separately by test_sass_homework_browser.cjs.
"""
from pathlib import Path
import copy,json,re,zipfile
import nbformat
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((ROOT/'reports/sass-homework-2026-10-01.json').read_text())

def verify(key, sources):
    doms=[BeautifulSoup(s.split('\n',2)[2], 'html.parser') for s in sources]
    for i,(source,d) in enumerate(zip(sources,doms)):
        assert source.startswith('%%html\n<!-- UI_RUNNER:')
        assert not d.select('style, link'), (key,'custom CSS')
        for e in d.select('[style]'):
            assert key=='grids' and i==1 and e['style']=='grid-template-columns: 1fr 1fr 1fr 2fr;'
        for e in d.select('[class]'):
            for c in e['class']:
                assert c.startswith(('ocs__','cols-')) or c in {'small','medium','large','gradient','pill','fill','outline','accent','alert-green','alert-yellow','alert-red'},(key,c)
        ids=[e['id'] for e in d.select('[id]')]
        assert len(ids)==len(set(ids))
        for e in d.select('label[for]'):assert d.find(id=e['for'])
    hw=doms[-1]
    if key=='typography':
        for d in doms:
            assert all(e.name in {'h1','h2','h3','h4','p','ol','ul','li','strong','em','div'} for e in d.find_all())
            assert d.select_one('h2.ocs__section-title') and d.select_one('h3') and d.select_one('p.ocs__lead')
        assert len(hw.select('ol'))==1 and len(hw.select('ol > li'))==3
        assert hw.strong.get_text()=='How to pat a cat:'
    if key=='inputs':
        assert len(doms[0].select('input'))==2
        fields=hw.select('input');assert len(fields)==3
        for e,size in zip(fields,['large','small','medium']):
            assert set(['ocs__input',size])<=set(e['class'])
            assert hw.select_one(f'label[for="{e["id"]}"]')
        assert 'gradient' in fields[0]['class'] and fields[-1]['type']=='email'
    if key=='buttons':
        assert len(doms)==5
        assert doms[0].select_one('a.ocs__btn')
        assert doms[1].select_one('.ocs__links button.ocs__btn.pill.fill')
        assert doms[2].select_one('.ocs__links--wide .alert-green')
        assert doms[2].select_one('.ocs__links--wide .alert-red.fill')
        for d in doms:
            for e in d.select('a'):assert e['href']=='https://www.mygoodbrain.org/resources'
            for e in d.select('button'):assert e['type']=='button'
        for d,required in [(doms[3],['alert-red.fill.pill','alert-green.fill.pill','accent.outline.pill']),(hw,['accent.fill','outline','alert-red.outline'])]:
            assert len(d.select('.ocs__links > .ocs__btn'))==3
            for cls in required:assert d.select_one('.ocs__links .ocs__btn.'+cls)
    if key=='containers':
        for d in doms:
            assert len(d.select('.ocs__container'))==len(d.select('.ocs__card'))==1
            assert d.select_one('.ocs__container > .ocs__card .ocs__section-title')
            assert d.select_one('.ocs__description')
            assert d.select_one('.ocs__grid.ocs__grid--standard.cols-3')
        assert len(doms[0].select('.ocs__grid > .ocs__grid-cell'))==3
        for c in ['header','accent','muted']:assert hw.select_one('.ocs__grid-cell--'+c)
        assert hw.select_one('.ocs__table-wrap > table.ocs__table')
        assert len(hw.select('thead tr'))==1 and len(hw.select('tbody tr'))==2
        assert hw.select_one('caption') and hw.select_one('th[scope="row"]') and hw.select_one('.ocs__callout')
    if key=='grids':
        assert len(doms[0].select('.ocs__grid.ocs__grid--standard > .ocs__grid-cell'))==3
        assert len(doms[1].select('.ocs__grid-cell'))==4
        assert doms[1].select('.ocs__grid-cell')[-1].text=='Control Beaker'
        grids=hw.select('.ocs__grid');assert len(grids)==2
        assert 'ocs__grid--standard' in grids[0]['class'] and 'ocs__grid--calculator' in grids[1]['class']
        for grid in grids:
            assert len([c for c in grid['class'] if c.startswith('ocs__grid--')])==1
            assert all('ocs__grid-cell' in e.get('class',[]) for e in grid.find_all(recursive=False))
        assert len(hw.select('.ocs__grid-cell'))==8
        assert grids[0].select_one('.ocs__grid-cell--header').text=='Temperature Trial (°C)'
        assert grids[0].select_one('.ocs__grid-cell--accent').text=='Beaker 3: 31.6'
        assert grids[1].select_one('.ocs__grid-cell--accent').text=='Avg'
    if key=='toggles':
        assert len(hw.select('label.ocs__toggle'))==3
        for t in hw.select('input[type="checkbox"]'):
            assert 'ocs__toggle-input' in t['class'] and t.find_parent('label')
            assert hw.find(id=t['aria-controls']).has_attr('hidden')
        assert hw.select_one('[role="status"][aria-live="polite"]')
        assert len(re.findall(r'^\s*//',sources[-1],re.M))>=4
    return doms

def main():
    cells=0;data={}
    for item in MANIFEST['submissions']:
        nb=nbformat.read(ROOT/item['file'],as_version=4);nbformat.validate(nb)
        code=[c for c in nb.cells if c.cell_type=='code'];assert len(code)==item['cells']
        sources=[c.source for c in code];verify(item['key'],sources);data[item['key']]=sources
        for c in code:
            assert c.execution_count and len(c.outputs)==1 and c.outputs[0].output_type=='display_data'
            assert c.outputs[0].data['text/html'].strip()==c.source.split('\n',1)[1].strip()
        prose='\n'.join(c.source for c in nb.cells if c.cell_type=='markdown')
        for phrase in ['Design thinking','Reviewer challenge','Rubric evidence','AI assistance','runners/ui.html']:assert phrase in prose
        assert not any('```' in c.source for c in nb.cells if c.cell_type=='markdown')
        cells+=len(code)
    # Real counterexamples: these errors must not accidentally qualify for full credit.
    mutations=[('typography','<strong>','<em>'),('inputs','ocs__input medium','medium'),('buttons','accent outline pill','accent fill pill'),('containers','ocs__grid-cell--muted','ocs__grid-cell--accent'),('grids','ocs__grid--calculator','ocs__grid--standard'),('grids','ocs__grid-cell--header','ocs__grid-cell--wide'),('toggles','aria-controls="uesl-debug-panel"','aria-controls="missing"')]
    for key,before,after in mutations:
        broken=copy.deepcopy(data[key]);assert before in broken[-1] or key=='buttons'
        broken=[s.replace(before,after) for s in broken]
        try:verify(key,broken)
        except (AssertionError,AttributeError):pass
        else:raise AssertionError(('undetected mutation',key,before))
    with zipfile.ZipFile(ROOT/'assets/homework/2026-10-01/sass-homework-notebooks.zip') as z:
        assert len(z.namelist())==7
        for i in MANIFEST['submissions']:assert z.read(Path(i['file']).name)==(ROOT/i['file']).read_bytes()
    print(f'PASS: 7 notebooks; {cells} saved HTML outputs; 7 rejected regressions; exact ZIP contents.')
if __name__=='__main__':main()
