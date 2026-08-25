import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(scriptDirectory, '..');
const lessonPath = path.join(repositoryRoot, '_posts/2026-08-19-pc-assembly-cpt-concepts.md');
const executorPath = path.join(repositoryRoot, 'assets/js/pages/runners/executors/PseudocodeExecutor.js');
const pyodideExecutorPath = path.join(repositoryRoot, 'assets/js/pages/runners/executors/PyodideExecutor.js');
const languageVariantManagerPath = path.join(repositoryRoot, 'assets/js/pages/runners/core/LanguageVariantManager.js');
const codeRunnerIncludePath = path.join(repositoryRoot, '_includes/runners/code.html');
const variantsPath = path.join(repositoryRoot, '_data/pc_assembly_runner_variants.yml');
const lesson = readFileSync(lessonPath, 'utf8');

function extractCapture(name) {
  const pattern = new RegExp('{% capture ' + name + ' %}\\n([\\s\\S]*?)\\n{% endcapture %}');
  const match = lesson.match(pattern);
  assert.ok(match, 'Missing Liquid capture: ' + name);
  return match[1];
}

const executorSource = readFileSync(executorPath, 'utf8');
const executorModule = await import(
  'data:text/javascript;base64,' + Buffer.from(executorSource).toString('base64')
);

function runPseudocodeSource(name, source, inputValues = []) {
  const pendingInputs = [...inputValues];
  globalThis.window = {
    prompt() {
      assert.ok(pendingInputs.length > 0, name + ' requested unexpected input');
      return pendingInputs.shift();
    },
  };

  const outputElement = { textContent: '' };
  const execTimeElement = { textContent: '' };
  const executor = new executorModule.PseudocodeExecutor({ outputElement, execTimeElement });
  executor.run(source);
  assert.equal(pendingInputs.length, 0, name + ' did not consume every test input');
  assert.doesNotMatch(outputElement.textContent, /^AP CSP (Runtime )?Error:/);
  return outputElement.textContent;
}

function runPseudocode(name, inputValues = []) {
  return runPseudocodeSource(name, extractCapture(name), inputValues);
}

const expectedPseudocodeOutputs = {
  pc_output_code: 'Current part: CPU\nInstall in: CPU socket',
  pc_input_code: 'Selected part: CPU\nSelected destination: CPU socket',
  pc_list_code: [
    'Parts in this build: 8',
    'CPU',
    'RAM',
    'M.2 SSD',
    'CPU cooler',
    'Motherboard',
    'Power supply',
    'Graphics card',
    'Power cables',
  ].join('\n'),
  pc_procedure_code: 'Correct placement: true',
  pc_sequence_code: [
    'Step 1: Seat the CPU',
    'Step 2: Install the RAM',
    'Step 3: Install the M.2 SSD',
    'Step 4: Mount the CPU cooler',
  ].join('\n'),
  pc_selection_code: 'Correct! CPU snapped into place.',
  pc_iteration_code: [
    'Step 1: Install CPU',
    'Step 2: Install RAM',
    'Step 3: Install M.2 SSD',
    'Step 4: Install CPU cooler',
    'Step 5: Install Motherboard',
    'Step 6: Install Power supply',
    'Step 7: Install Graphics card',
    'Step 8: Install Power cables',
  ].join('\n'),
  pc_algorithm_code: [
    'Graphics card returned. Next part is CPU.',
    'CPU installed correctly.',
    'RAM installed correctly.',
    'M.2 SSD installed correctly.',
    'CPU cooler installed correctly.',
    'Installed correctly: 4 of 4',
  ].join('\n'),
  pc_list_operations_code: [
    'Initial tray: CPU,RAM',
    'After APPEND: CPU,RAM,M.2 SSD',
    'After INSERT: CPU,CPU cooler,RAM,M.2 SSD',
    'After installing CPU: CPU cooler,RAM,M.2 SSD',
    'Parts remaining: 3',
  ].join('\n'),
  pc_search_code: 'Graphics card position: 4',
  pc_boolean_code: 'The CPU snaps into place.\nThe PC build is still in progress.',
};

const pseudocodeInputs = {
  pc_input_code: ['CPU', 'CPU socket'],
  pc_selection_code: ['CPU'],
};

for (const [name, expectedOutput] of Object.entries(expectedPseudocodeOutputs)) {
  assert.equal(runPseudocode(name, pseudocodeInputs[name]), expectedOutput, name + ' output changed');
}

assert.match(lesson, /^---[\s\S]*?search_exclude:\s*false[\s\S]*?---/);
assert.doesNotMatch(lesson, /id="view-(python|javascript|both)"/);
assert.equal((lesson.match(/language="pseudocode"/g) || []).length, 11);
assert.equal(
  (lesson.match(/variants_key="[a-z_]+"/g) || []).length,
  12,
  'Every concept runner and the full prototype must provide language variants',
);
assert.doesNotMatch(lesson, /lock_language=true/);
assert.equal((lesson.match(/local_python=true/g) || []).length, 12);

const yamlRead = spawnSync('ruby', [
  '-ryaml',
  '-rjson',
  '-e',
  'puts JSON.generate(YAML.load_file(ARGV.fetch(0)))',
  variantsPath,
], { encoding: 'utf8' });
assert.equal(yamlRead.status, 0, yamlRead.stderr);
const languageVariants = JSON.parse(yamlRead.stdout);
const conceptVariantKeys = [
  'output',
  'input',
  'list',
  'procedure',
  'sequence',
  'selection',
  'iteration',
  'algorithm',
  'list_operations',
  'search',
  'boolean',
];

for (const key of conceptVariantKeys) {
  assert.ok(languageVariants[key]?.python, key + ' is missing Python code');
  assert.ok(languageVariants[key]?.java, key + ' is missing Java code');

  const pythonRun = spawnSync('python3', ['-c', languageVariants[key].python], {
    cwd: repositoryRoot,
    encoding: 'utf8',
  });
  assert.equal(pythonRun.status, 0, `${key} Python failed:\n${pythonRun.stderr}`);
}

assert.ok(languageVariants.prototype?.pseudocode, 'Full prototype is missing Pseudocode code');
assert.ok(languageVariants.prototype?.java, 'Full prototype is missing Java code');
const prototypePseudocodeOutput = runPseudocodeSource(
  'prototype pseudocode',
  languageVariants.prototype.pseudocode,
);
assert.match(prototypePseudocodeOutput, /Build complete!/);
assert.match(prototypePseudocodeOutput, /Accuracy: 8 of 9$/);
assert.match(prototypePseudocodeOutput, /Incorrect: Graphics card returned to the parts tray\./);

const javaVariants = [
  ...conceptVariantKeys.map((key) => [key, languageVariants[key].java]),
  ['prototype', languageVariants.prototype.java],
];

for (const [key, source] of javaVariants) {
  assert.match(source, /public class Main\s*\{/);
  assert.match(source, /public static void main\(String\[\] args\)/);
  assert.equal((source.match(/{/g) || []).length, (source.match(/}/g) || []).length, key + ' Java braces do not balance');
}

const javacCheck = spawnSync('javac', ['-version'], { encoding: 'utf8' });
if (javacCheck.status === 0) {
  for (const [key, source] of javaVariants) {
    const tempDirectory = mkdtempSync(path.join(os.tmpdir(), 'pc-java-'));
    try {
      writeFileSync(path.join(tempDirectory, 'Main.java'), source);
      const compile = spawnSync('javac', ['Main.java'], { cwd: tempDirectory, encoding: 'utf8' });
      assert.equal(compile.status, 0, `${key} Java failed to compile:\n${compile.stderr}`);
    } finally {
      rmSync(tempDirectory, { recursive: true, force: true });
    }
  }
}

const javascriptPrototype = extractCapture('pc_javascript_code');
const runJavascriptPrototype = new Function('outputElement', 'document', javascriptPrototype);
for (const requiredBehavior of [
  "partCard.draggable = true",
  "addEventListener('drop'",
  'function checkPlacement(partIndex, slotIndex)',
  'attempts.push(isCorrect)',
  'returned to the tray',
  'snapped into place',
  "setAttribute('aria-live', 'polite')",
  "document.getElementById('pc-builder-name')",
  "pc-part-shape--",
  "data-slot-index",
  "pc-board-ghost",
  "pc-fan--",
]) {
  assert.ok(javascriptPrototype.includes(requiredBehavior), 'Missing JavaScript behavior: ' + requiredBehavior);
}

class FakeElement {
  constructor(tagName) {
    this.tagName = tagName;
    this.children = [];
    this.style = {};
    this.listeners = new Map();
    this.attributes = new Map();
    this.textContent = '';
    this.value = '';
    this.disabled = false;
    this.draggable = false;
    this.firstChild = null;
  }

  appendChild(child) {
    this.children.push(child);
    this.firstChild = this.children[0] || null;
    return child;
  }

  insertBefore(child, before) {
    const index = this.children.indexOf(before);
    if (index === -1) {
      return this.appendChild(child);
    }
    this.children.splice(index, 0, child);
    this.firstChild = this.children[0] || null;
    return child;
  }

  setAttribute(name, value) {
    this.attributes.set(name, value);
  }

  addEventListener(type, listener) {
    if (!this.listeners.has(type)) {
      this.listeners.set(type, []);
    }
    this.listeners.get(type).push(listener);
  }

  dispatch(type, event = {}) {
    for (const listener of this.listeners.get(type) || []) {
      listener(event);
    }
  }
}

const createdElements = [];
const fakeDocument = {
  createElement(tagName) {
    const element = new FakeElement(tagName);
    createdElements.push(element);
    return element;
  },
  getElementById(id) {
    return createdElements.find((element) => element.id === id) || null;
  },
};

const uiOutput = new FakeElement('div');
runJavascriptPrototype(uiOutput, fakeDocument);
const app = createdElements.find((element) => element.className === 'pc-assembly-app');
const status = createdElements.find((element) => element.className === 'pc-status');
const progress = createdElements.find((element) => element.className === 'pc-progress');
const partCards = createdElements.filter((element) => element.attributes.has('data-part-index'));
const slotButtons = createdElements.filter((element) => element.attributes.has('data-slot-index'));
const resetButton = createdElements.find((element) => element.className === 'pc-reset');

assert.ok(app, 'PC assembly app was not created');
assert.equal(partCards.length, 8);
assert.equal(slotButtons.length, 8);
assert.equal(status.textContent, 'Next part: CPU');
assert.equal(progress.textContent, 'Installed 0 of 8 • Accuracy 100%');

partCards[6].dispatch('click');
slotButtons[6].dispatch('click');
assert.match(status.textContent, /Graphics card returned to the tray/);
assert.equal(partCards[6].disabled, false);
assert.equal(progress.textContent, 'Installed 0 of 8 • Accuracy 0%');

partCards[0].dispatch('click');
slotButtons[0].dispatch('click');
assert.equal(partCards[0].disabled, true);
assert.equal(slotButtons[0].disabled, true);
assert.match(slotButtons[0].textContent, /^✓ CPU$/);
assert.equal(progress.textContent, 'Installed 1 of 8 • Accuracy 50%');

resetButton.dispatch('click');
assert.equal(partCards[0].disabled, false);
assert.equal(slotButtons[0].disabled, false);
assert.equal(progress.textContent, 'Installed 0 of 8 • Accuracy 100%');

const dragData = new Map();
const dataTransfer = {
  setData(type, value) {
    dragData.set(type, value);
  },
  getData(type) {
    return dragData.get(type) || '';
  },
};
partCards[0].dispatch('dragstart', { dataTransfer });
slotButtons[0].dispatch('drop', { dataTransfer, preventDefault() {} });
assert.equal(partCards[0].disabled, true);
assert.equal(progress.textContent, 'Installed 1 of 8 • Accuracy 100%');

for (let index = 1; index < partCards.length; index += 1) {
  partCards[index].dispatch('click');
  slotButtons[index].dispatch('click');
}
assert.equal(status.textContent, 'PC assembly complete!');
assert.equal(progress.textContent, 'Installed 8 of 8 • Accuracy 100%');

resetButton.dispatch('click');
const unrelatedDragData = { getData() { return ''; } };
slotButtons[0].dispatch('drop', { dataTransfer: unrelatedDragData, preventDefault() {} });
assert.equal(status.textContent, 'Choose a part from the tray first.');
assert.equal(progress.textContent, 'Installed 0 of 8 • Accuracy 100%');

const pythonPrototype = extractCapture('pc_python_code');
const pythonRun = spawnSync('python3', ['-c', pythonPrototype], {
  cwd: repositoryRoot,
  encoding: 'utf8',
});
assert.equal(pythonRun.status, 0, pythonRun.stderr);
assert.match(pythonRun.stdout, /PC assembly complete!\nAccuracy: 89%\s*$/);
assert.match(pythonRun.stdout, /Incorrect placement\. The part returned to the tray\./);

assert.match(
  lesson,
  /runner_id="pc-python"[\s\S]*?language="python"[\s\S]*?local_python=true[\s\S]*?%}/,
  'The Python prototype must use browser-local execution',
);

const codeRunnerInclude = readFileSync(codeRunnerIncludePath, 'utf8');
assert.match(codeRunnerInclude, /localPythonExecutor\.run\(editor\.getValue\(\)\)/);
assert.match(codeRunnerInclude, /data-python-code=/);
assert.match(codeRunnerInclude, /data-java-code=/);
assert.match(codeRunnerInclude, /data-pseudocode-code=/);
assert.match(codeRunnerInclude, /languageVariants\?\.switchTo\(lang\)/);

const managerSource = readFileSync(languageVariantManagerPath, 'utf8');
const managerModule = await import(
  'data:text/javascript;base64,' + Buffer.from(managerSource).toString('base64')
);
const savedDrafts = new Map();
globalThis.localStorage = {
  getItem(key) { return savedDrafts.has(key) ? savedDrafts.get(key) : null; },
  setItem(key, value) { savedDrafts.set(key, value); },
  removeItem(key) { savedDrafts.delete(key); },
};
const fakeEditor = {
  value: '',
  mode: '',
  refreshCount: 0,
  getValue() { return this.value; },
  setValue(value) { this.value = value; },
  setOption(name, value) { if (name === 'mode') this.mode = value; },
  refresh() { this.refreshCount += 1; },
};
const fakeLanguageSelect = { value: '' };
const draftManager = new managerModule.LanguageVariantManager({
  editor: fakeEditor,
  languageSelect: fakeLanguageSelect,
  variants: { pseudocode: 'DISPLAY("CPU")', python: 'print("CPU")', java: 'class Main {}' },
  storageKey: 'pc-output',
  initialLanguage: 'pseudocode',
});
draftManager.activateInitial();
assert.equal(fakeEditor.value, 'DISPLAY("CPU")');
assert.equal(fakeEditor.mode, 'pseudocode');
fakeEditor.value = 'DISPLAY("edited")';
assert.equal(draftManager.switchTo('python'), true);
assert.equal(fakeEditor.value, 'print("CPU")');
assert.equal(fakeEditor.mode, 'python');
fakeEditor.value = 'print("edited")';
draftManager.saveCurrent();
assert.equal(savedDrafts.get('pc-output_python'), 'print("edited")');
draftManager.switchTo('pseudocode');
assert.equal(fakeEditor.value, 'DISPLAY("edited")', 'Unsaved edits must survive language switching');
draftManager.clearAll();
draftManager.resetCurrent();
assert.equal(fakeEditor.value, 'DISPLAY("CPU")');
assert.equal(savedDrafts.size, 0);

const browserPythonCalls = [];
const fakeBrowserPython = {
  runPython(code) {
    browserPythonCalls.push(code);
    if (code === '__runner_output.getvalue()') {
      return 'PC assembly complete!\nAccuracy: 89%\n';
    }
    return undefined;
  },
};
let runtimeLoads = 0;
globalThis.loadPyodide = async ({ indexURL }) => {
  runtimeLoads += 1;
  assert.equal(indexURL, 'https://cdn.jsdelivr.net/pyodide/v0.23.4/full/');
  return fakeBrowserPython;
};

const pyodideExecutorSource = readFileSync(pyodideExecutorPath, 'utf8');
const pyodideExecutorModule = await import(
  'data:text/javascript;base64,' + Buffer.from(pyodideExecutorSource).toString('base64')
);
const browserPythonOutput = { textContent: '' };
const browserPythonTime = { textContent: '' };
const browserPythonExecutor = new pyodideExecutorModule.PyodideExecutor({
  outputElement: browserPythonOutput,
  execTimeElement: browserPythonTime,
});
await browserPythonExecutor.run(pythonPrototype);
assert.equal(runtimeLoads, 1);
assert.ok(browserPythonCalls.includes(pythonPrototype));
assert.equal(browserPythonOutput.textContent, 'PC assembly complete!\nAccuracy: 89%\n');
assert.match(browserPythonTime.textContent, /\(browser\)$/);
delete globalThis.loadPyodide;
delete globalThis.localStorage;

console.log('PC assembly lesson checks passed: 12 three-language runners, JavaScript prototype, and browser Python.');
