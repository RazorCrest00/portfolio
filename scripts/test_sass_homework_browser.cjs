/* Run with Playwright available on NODE_PATH; BASE defaults to the local preview.
 * Uses real OCS styles, shared editor and UI executor; only unrelated auth is isolated.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const assert = require('node:assert/strict');
const path = require('path');
const root = path.resolve(__dirname, '..');
const manifest = JSON.parse(fs.readFileSync(path.join(root,'reports/sass-homework-2026-10-01.json')));
const base = process.env.BASE || 'http://127.0.0.1:4630/portfolio';
const shots = process.env.SCREENSHOTS;
(async()=>{
 const browser = await chromium.launch({channel:'chrome',headless:true});
 const context = await browser.newContext({viewport:{width:1440,height:1000}});
 await context.route('**/api/**',r=>r.fulfill({status:401,contentType:'application/json',body:'{}'}));
 if(fs.existsSync('/tmp/uesl-mermaid-10.js')) await context.route('https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js',r=>r.fulfill({path:'/tmp/uesl-mermaid-10.js',contentType:'application/javascript'}));
 const page = await context.newPage();let errors=[];page.on('pageerror',e=>errors.push(e.message));
 const results=[];
 for(const item of manifest.submissions){
  errors=[];
  await page.goto(base+'/sass/'+item.key+'-hw/',{waitUntil:'domcontentloaded'});
  await page.waitForSelector('#ui-runner-sass-hw-'+item.key+' .CodeMirror');
  const lab=page.locator('#ui-runner-sass-hw-'+item.key), output=lab.locator('.ui-output');
  await lab.locator('[data-hook="run"]').click();
  await page.waitForFunction(k=>document.querySelector('#ui-output-sass-hw-'+k).textContent.trim().length>0,item.key);
  assert(!/^Error:/.test((await output.innerText()).trim()),item.key+' runtime');
  assert.equal(await page.locator('.ui-runner-container').count(),item.cells);
  assert.equal(await page.locator('.ui-runner').count(),0);
  for(const runner of await page.locator('.ui-runner-container').all()){
   await runner.locator('[data-hook="run"]').click();
   assert((await runner.locator('.ui-output').innerText()).trim());
   assert(!/^Error:/.test((await runner.locator('.ui-output').innerText()).trim()));
   const cm=runner.locator('.CodeMirror');
   const saved=await cm.evaluate(e=>e.CodeMirror.getValue());
   await cm.evaluate(e=>e.CodeMirror.setValue(e.CodeMirror.getValue()+'\noutputElement.append(document.createTextNode("Per-cell edit verified"));'));
   await runner.locator('[data-hook="run"]').click();assert((await runner.locator('.ui-output').innerText()).includes('Per-cell edit verified'));
   await runner.locator('[data-hook="clear"]').click();assert.equal(await cm.evaluate(e=>e.CodeMirror.getValue()),saved);
   await runner.locator('[data-hook="run"]').click();
  }
  const dupes=await page.evaluate(()=>{const a=[...document.querySelectorAll('[id]')].map(x=>x.id);return a.filter((x,i)=>a.indexOf(x)!==i)});
  assert.deepEqual(dupes,[],item.key+' duplicate ids');
  const original=await lab.locator('.CodeMirror').evaluate(e=>e.CodeMirror.getValue());
  // Editing, rendering, output reset and restoring source exercise the actual shared runner.
  await lab.locator('.CodeMirror').evaluate(e=>e.CodeMirror.setValue(e.CodeMirror.getValue()+'\noutputElement.append(document.createTextNode("Reviewer edit verified"));'));
  await lab.locator('[data-hook="run"]').click();assert((await output.innerText()).includes('Reviewer edit verified'));
  await lab.locator('[data-hook="reset"]').click();assert.equal(await output.innerText(),'');
  await lab.locator('[data-hook="clear"]').click();
  assert.equal(await lab.locator('.CodeMirror').evaluate(e=>e.CodeMirror.getValue()),original);
  await lab.locator('[data-hook="run"]').click();
  if(item.key==='grids'){
   assert.equal(await output.locator('[aria-label="Homework checks"] li').count(),8);
   assert(!(await output.innerText()).includes('FIX —'));
   await lab.locator('.CodeMirror').evaluate(e=>e.CodeMirror.setValue(e.CodeMirror.getValue().replace('ocs__grid-cell ocs__grid-cell--header','ocs__grid-cell')));
   await lab.locator('[data-hook="run"]').click();
   assert((await output.innerText()).includes('FIX — Title is a header cell'));
   await lab.locator('[data-hook="clear"]').click();await lab.locator('[data-hook="run"]').click();
   assert(!(await output.innerText()).includes('FIX —'));
  }
  if(item.key==='toggles'){
   for(const prefix of ['']){
    const toggles=page.locator('#'+prefix+'uesl-settings input[type="checkbox"]');
    for(let mask=0;mask<8;mask++){
     for(let i=0;i<3;i++) await toggles.nth(i).evaluate((e,v)=>{e.checked=v;e.dispatchEvent(new Event('change',{bubbles:true}))},!!(mask&(1<<i)));
     assert.equal(await page.locator('#'+prefix+'uesl-count').innerText(),mask.toString(2).replace(/0/g,'').length+' of 3 features enabled');
     for(let i=0;i<3;i++){const panel=await toggles.nth(i).getAttribute('aria-controls');assert.equal(await page.locator('#'+panel).isVisible(),!!(mask&(1<<i)))}
    }
    await page.locator('#'+prefix+'uesl-reset').click();assert.equal(await page.locator('#'+prefix+'uesl-count').innerText(),'0 of 3 features enabled');
    await toggles.nth(0).focus();await page.keyboard.press('Space');assert.equal(await toggles.nth(0).isChecked(),true);
    await page.locator('#'+prefix+'uesl-reset').click();
   }
  }
  if(item.key==='inputs'){
   for(const prefix of ['']){
    const email=page.locator('#'+prefix+'pvo-email');await email.fill('invalid');assert(await email.evaluate(e=>e.validity.typeMismatch));
    await email.fill('student@example.com');assert(await email.evaluate(e=>e.checkValidity()));
    await email.fill('');assert(await email.evaluate(e=>e.validity.valueMissing));
    for(const id of ['pvo-category','pvo-name','pvo-email']){await page.locator('label[for="'+prefix+id+'"]').click();assert.equal(await page.evaluate(()=>document.activeElement.id),prefix+id)}
   }
  }
  if(item.key==='buttons'||item.key==='guide'){
   const button=output.locator('button').first();await button.focus();await page.keyboard.press('Enter');assert((await button.innerText()).includes('(demo)'));
   await lab.locator('[data-hook="run"]').click();await output.locator('button').first().focus();await page.keyboard.press('Space');assert((await output.locator('button').first().innerText()).includes('(demo)'));
   await lab.locator('[data-hook="run"]').click();
  }
  const sizes=[];
  for(const width of [1440,390]){
   await page.setViewportSize({width,height:1000});await page.waitForTimeout(200);
   const dims=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));
   sizes.push(dims);assert(dims.scroll<=width+1,item.key+' page overflow '+JSON.stringify(dims));
   if(item.key==='containers'){
    const tracks=await output.locator('.ocs__grid').evaluate(e=>getComputedStyle(e).gridTemplateColumns.split(' ').length);
    assert.equal(tracks,width===1440?3:2);
   }
   if(item.key==='grids'&&width===1440){
    const widths=await page.locator('#sass-grids-exercise-2 .ocs__grid-cell').evaluateAll(es=>es.map(e=>e.getBoundingClientRect().width));
    assert(Math.abs(widths[3]/widths[0]-2)<.03,JSON.stringify(widths));
   }
   if(shots){fs.mkdirSync(shots,{recursive:true});await output.screenshot({path:path.join(shots,item.key+'-'+width+'.png')});}
  }
  assert.deepEqual(errors,[],item.key+' page errors');
  results.push({key:item.key,outputs:item.cells,runner:true,editReset:true,sizes});console.log('PASS',item.key);
 }
 await page.goto(base+'/homework/sass/');assert.equal(await page.locator('a[href$=".ipynb"]').count(),7);
 fs.writeFileSync(process.env.RESULTS||'/tmp/sass-browser-results.json',JSON.stringify({base,results},null,2));
 await browser.close();console.log('PASS: all browser labs, behavior, keyboard, source reset, output reset and responsive checks.');
})().catch(e=>{console.error(e);process.exit(1)});
