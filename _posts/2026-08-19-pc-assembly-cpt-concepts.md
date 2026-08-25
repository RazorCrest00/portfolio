---
layout: post
codemirror: true
title: "PC Assembly: Create Performance Task Concepts"
description: Learn every AP CSP Create Performance Task concept through one PC assembly theme.
permalink: /pc-assembly
search_exclude: false
---

# PC Assembly: Create Performance Task Concepts

**Team:** Adhvay Iyer, Rohan Chandra, Ishan Shrivastava, Ishan Jha, Ishan Khandelwal, and Vayun Shekhar

This notebook uses one theme throughout: assembling the parts of a desktop computer in the correct order. The user chooses a component and its destination. A correct component snaps into place; an incorrect component returns to the parts tray. Every example below connects that program idea to a CPT requirement.

# Code Runner Concepts

Each runner starts in College Board pseudocode. Use the language dropdown to switch the entire example between Pseudocode, Python, and Java. Each language keeps its own edited draft while you switch.

---

## Output

**CPT Requirement:** Your program must produce output visible to the user. College Board pseudocode uses `DISPLAY()` to show results. In the PC assembly program, output tells the builder which part is next and whether a placement was correct.

{% capture pc_output_challenge %}
Display the current PC part and where it should be installed.
{% endcapture %}

{% capture pc_output_code %}
currentPart ← "CPU"
targetSlot ← "CPU socket"

DISPLAY("Current part: " + currentPart)
DISPLAY("Install in: " + targetSlot)
{% endcapture %}

{% include runners/code.html
  runner_id="pc-output"
  language="pseudocode"
  variants_key="output"
  local_python=true
  challenge=pc_output_challenge
  code=pc_output_code
  height="220px"
%}

**Expected output**

```text
Current part: CPU
Install in: CPU socket
```

---

## Input

**CPT Requirement:** Your program must get input from the user. College Board pseudocode uses `INPUT()` to collect data. In this project, the builder supplies a part and a destination.

{% capture pc_input_challenge %}
Ask the builder to choose a PC part and its destination, then display both choices.
{% endcapture %}

{% capture pc_input_code %}
selectedPart ← INPUT("Choose a PC part:")
selectedSlot ← INPUT("Choose its destination:")

DISPLAY("Selected part: " + selectedPart)
DISPLAY("Selected destination: " + selectedSlot)
{% endcapture %}

{% include runners/code.html
  runner_id="pc-input"
  language="pseudocode"
  variants_key="input"
  local_python=true
  challenge=pc_input_challenge
  code=pc_input_code
  height="230px"
%}

**Example output (if the user chose "CPU" and "CPU socket")**

```text
Selected part: CPU
Selected destination: CPU socket
```

---

## List

**CPT Requirement:** Your program must use a list to manage multiple related values. The ordered `parts` list stores every component without requiring a separate variable for each one. College Board pseudocode lists begin at index 1.

{% capture pc_list_challenge %}
Store the PC components in assembly order and display each component with a loop.
{% endcapture %}

{% capture pc_list_code %}
parts ← ["CPU", "RAM", "M.2 SSD", "CPU cooler", "Motherboard", "Power supply", "Graphics card", "Power cables"]

DISPLAY("Parts in this build: " + LENGTH(parts))

FOR EACH part IN parts
{
  DISPLAY(part)
}
{% endcapture %}

{% include runners/code.html
  runner_id="pc-list"
  language="pseudocode"
  variants_key="list"
  local_python=true
  challenge=pc_list_challenge
  code=pc_list_code
  height="300px"
%}

**Expected output**

```text
Parts in this build: 8
CPU
RAM
M.2 SSD
CPU cooler
Motherboard
Power supply
Graphics card
Power cables
```

---

## Procedure

**CPT Requirement:** You must create at least one student-developed procedure with parameters. The procedure must be called and contribute to the program. This procedure accepts a part and a target, then returns whether they match.

{% capture pc_procedure_challenge %}
Create and call a procedure that checks whether the CPU was placed in the CPU socket.
{% endcapture %}

{% capture pc_procedure_code %}
PROCEDURE isCorrectTarget(partName, targetName)
{
  RETURN(partName = "CPU" AND targetName = "CPU socket")
}

correctPlacement ← isCorrectTarget("CPU", "CPU socket")
DISPLAY("Correct placement: " + correctPlacement)
{% endcapture %}

{% include runners/code.html
   runner_id="pc-procedure"
   language="pseudocode"
   variants_key="procedure"
   local_python=true
   challenge=pc_procedure_challenge
   code=pc_procedure_code
   height="390px"
%}

**Expected output**

```text
Correct placement: true
```

---

## Sequence

**CPT Concept:** Sequencing means statements execute in order. A PC must also be assembled in a sensible order: prepare the motherboard, mount it, and then connect the remaining components.

{% capture pc_sequence_challenge %}
Display four motherboard-preparation steps in the order they occur.
{% endcapture %}

{% capture pc_sequence_code %}
step ← 1
DISPLAY("Step " + step + ": Seat the CPU")

step ← step + 1
DISPLAY("Step " + step + ": Install the RAM")

step ← step + 1
DISPLAY("Step " + step + ": Install the M.2 SSD")

step ← step + 1
DISPLAY("Step " + step + ": Mount the CPU cooler")
{% endcapture %}

{% include runners/code.html
  runner_id="pc-sequence"
  language="pseudocode"
  variants_key="sequence"
  local_python=true
  challenge=pc_sequence_challenge
  code=pc_sequence_code
  height="330px"
%}

**Expected output**

```text
Step 1: Seat the CPU
Step 2: Install the RAM
Step 3: Install the M.2 SSD
Step 4: Mount the CPU cooler
```

---

## Selection

**CPT Requirement:** Your algorithm must include selection with `IF` or `IF/ELSE`. Selection lets the program keep a correct part in place or return an incorrect part to the tray.

{% capture pc_selection_challenge %}
Check a selected component. If it is the expected part, snap it in; otherwise return it to the tray.
{% endcapture %}

{% capture pc_selection_code %}
expectedPart ← "CPU"
selectedPart ← INPUT("Choose the first part:")

IF (selectedPart = expectedPart)
{
  DISPLAY("Correct! " + selectedPart + " snapped into place.")
}
ELSE
{
  DISPLAY("Incorrect. " + selectedPart + " returned to the parts tray.")
  DISPLAY("Install " + expectedPart + " first.")
}
{% endcapture %}

{% include runners/code.html
   runner_id="pc-selection"
   language="pseudocode"
   variants_key="selection"
   local_python=true
   challenge=pc_selection_challenge
   code=pc_selection_code
   height="360px"
%}

**Example output (if the user selected "CPU")**

```text
Correct! CPU snapped into place.
```

---

## Iteration

**CPT Requirement:** Your algorithm must include iteration using a loop. Iteration lets one block of code process every PC component instead of repeating similar statements eight times.

{% capture pc_iteration_challenge %}
Loop through the ordered parts list and display one installation instruction for each component.
{% endcapture %}

{% capture pc_iteration_code %}
parts ← ["CPU", "RAM", "M.2 SSD", "CPU cooler", "Motherboard", "Power supply", "Graphics card", "Power cables"]
step ← 1

FOR EACH part IN parts
{
  DISPLAY("Step " + step + ": Install " + part)
  step ← step + 1
}
{% endcapture %}

{% include runners/code.html
  runner_id="pc-iteration"
  language="pseudocode"
  variants_key="iteration"
  local_python=true
  challenge=pc_iteration_challenge
  code=pc_iteration_code
  height="320px"
%}

**Expected output**

```text
Step 1: Install CPU
Step 2: Install RAM
Step 3: Install M.2 SSD
Step 4: Install CPU cooler
Step 5: Install Motherboard
Step 6: Install Power supply
Step 7: Install Graphics card
Step 8: Install Power cables
```

---

## Complete Algorithm

**CPT Requirement:** Your main algorithm must integrate sequencing, selection, and iteration to solve a meaningful problem. This procedure processes a list in order, checks each simulated placement, records the result, and returns the number of successful installations.

{% capture pc_algorithm_challenge %}
Run a complete PC assembly algorithm that combines a list, procedure, sequence, selection, iteration, and a return value.
{% endcapture %}

{% capture pc_algorithm_code %}
PROCEDURE assembleComputer(parts, selectedParts)
{
  installedCount ← 0
  step ← 1

  FOR EACH selectedPart IN selectedParts
  {
    expectedPart ← parts[step]

    IF (selectedPart = expectedPart)
    {
      DISPLAY(selectedPart + " installed correctly.")
      installedCount ← installedCount + 1
      step ← step + 1
    }
    ELSE
    {
      DISPLAY(selectedPart + " returned. Next part is " + expectedPart + ".")
    }
  }

  RETURN(installedCount)
}

parts ← ["CPU", "RAM", "M.2 SSD", "CPU cooler"]
attempts ← ["Graphics card", "CPU", "RAM", "M.2 SSD", "CPU cooler"]
installed ← assembleComputer(parts, attempts)
DISPLAY("Installed correctly: " + installed + " of " + LENGTH(parts))
{% endcapture %}

{% include runners/code.html
   runner_id="pc-algorithm"
   language="pseudocode"
   variants_key="algorithm"
   local_python=true
   challenge=pc_algorithm_challenge
   code=pc_algorithm_code
   height="600px"
%}

**Expected output**

```text
Graphics card returned. Next part is CPU.
CPU installed correctly.
RAM installed correctly.
M.2 SSD installed correctly.
CPU cooler installed correctly.
Installed correctly: 4 of 4
```

---

## List Operations

**AP CSP Concept:** `APPEND`, `INSERT`, `REMOVE`, and `LENGTH` modify and measure lists. These operations can update the parts tray as components are added or installed.

{% capture pc_list_operations_challenge %}
Modify a PC parts tray with all four College Board list operations.
{% endcapture %}

{% capture pc_list_operations_code %}
partsTray ← ["CPU", "RAM"]
DISPLAY("Initial tray: " + partsTray)

APPEND(partsTray, "M.2 SSD")
DISPLAY("After APPEND: " + partsTray)

INSERT(partsTray, 2, "CPU cooler")
DISPLAY("After INSERT: " + partsTray)

REMOVE(partsTray, 1)
DISPLAY("After installing CPU: " + partsTray)

DISPLAY("Parts remaining: " + LENGTH(partsTray))
{% endcapture %}

{% include runners/code.html
  runner_id="pc-list-operations"
  language="pseudocode"
  variants_key="list_operations"
  local_python=true
  challenge=pc_list_operations_challenge
  code=pc_list_operations_code
  height="380px"
%}

**Expected output**

```text
Initial tray: CPU,RAM
After APPEND: CPU,RAM,M.2 SSD
After INSERT: CPU,CPU cooler,RAM,M.2 SSD
After installing CPU: CPU cooler,RAM,M.2 SSD
Parts remaining: 3
```

---

## Search Algorithm

**AP CSP Concept:** A linear search checks every list item until it finds a target. This algorithm searches the parts tray and returns its 1-based position, or `-1` when the part is absent.

{% capture pc_search_challenge %}
Search the parts tray for the graphics card and display its position.
{% endcapture %}

{% capture pc_search_code %}
PROCEDURE findPart(partsTray, targetPart)
{
  position ← 1

  FOR EACH part IN partsTray
  {
    IF (part = targetPart)
    {
      RETURN(position)
    }
    position ← position + 1
  }

  RETURN(-1)
}

partsTray ← ["CPU", "RAM", "M.2 SSD", "Graphics card"]
result ← findPart(partsTray, "Graphics card")
DISPLAY("Graphics card position: " + result)
{% endcapture %}

{% include runners/code.html
   runner_id="pc-search"
   language="pseudocode"
   variants_key="search"
   local_python=true
   challenge=pc_search_challenge
   code=pc_search_code
   height="480px"
%}

**Expected output**

```text
Graphics card position: 4
```

---

## Boolean Logic

**AP CSP Concept:** `AND`, `OR`, and `NOT` combine Boolean conditions. A part should snap in only when both the component and its destination are correct. The build is not finished while required parts remain.

{% capture pc_boolean_challenge %}
Use AND and NOT to decide whether a CPU should snap into place and whether the build is still in progress.
{% endcapture %}

{% capture pc_boolean_code %}
selectedPart ← "CPU"
selectedSlot ← "CPU socket"
expectedPart ← "CPU"
expectedSlot ← "CPU socket"
partsRemaining ← 7

correctPart ← selectedPart = expectedPart
correctSlot ← selectedSlot = expectedSlot

IF (correctPart AND correctSlot)
{
  DISPLAY("The CPU snaps into place.")
}
ELSE
{
  DISPLAY("Return the part to the tray.")
}

IF (NOT (partsRemaining = 0))
{
  DISPLAY("The PC build is still in progress.")
}
{% endcapture %}

{% include runners/code.html
   runner_id="pc-boolean"
   language="pseudocode"
   variants_key="boolean"
   local_python=true
   challenge=pc_boolean_challenge
   code=pc_boolean_code
   height="500px"
%}

**Expected output**

```text
The CPU snaps into place.
The PC build is still in progress.
```

---

# JavaScript Prototype

The JavaScript version turns the algorithm into a browser interaction. Drag each component from the parts tray to its matching connection point in assembly order. Clicking a part and then a slot provides the same interaction for keyboard and touch users. Correct placements snap into the build; incorrect placements stay in the tray. The program records every attempt and displays the current accuracy.

{% capture pc_javascript_challenge %}
Run the PC assembly prototype. Try a wrong part first, then install all eight components in order. Identify the input, output, lists, procedure, selection, iteration, and Boolean expression in the code.
{% endcapture %}

{% capture pc_javascript_code %}
outputElement.innerHTML = '';

const parts = [
  { name: 'CPU', slot: 'CPU socket', kind: 'cpu', left: 34, top: 24, width: 14, height: 15, layer: 6 },
  { name: 'RAM', slot: 'RAM slots', kind: 'ram', left: 55, top: 17, width: 10, height: 32, layer: 5 },
  { name: 'M.2 SSD', slot: 'M.2 slot', kind: 'ssd', left: 39, top: 53, width: 25, height: 8, layer: 5 },
  { name: 'CPU cooler', slot: 'Cooler mount', kind: 'cooler', left: 27, top: 15, width: 28, height: 34, layer: 4 },
  { name: 'Motherboard', slot: 'Board tray', kind: 'motherboard', left: 17, top: 9, width: 60, height: 58, layer: 2 },
  { name: 'Power supply', slot: 'PSU bay', kind: 'psu', left: 5, top: 76, width: 31, height: 18, layer: 4 },
  { name: 'Graphics card', slot: 'PCIe slot', kind: 'gpu', left: 24, top: 65, width: 57, height: 12, layer: 5 },
  { name: 'Power cables', slot: 'Power headers', kind: 'cables', left: 79, top: 24, width: 13, height: 47, layer: 5 }
];

const attempts = [];
let currentStep = 0;
let selectedPart = -1;

const app = document.createElement('section');
const styleElement = document.createElement('style');
const header = document.createElement('div');
const titleGroup = document.createElement('div');
const heading = document.createElement('h3');
const directions = document.createElement('p');
const controls = document.createElement('div');
const nameLabel = document.createElement('label');
const builderName = document.createElement('input');
const liveRow = document.createElement('div');
const status = document.createElement('p');
const progress = document.createElement('p');
const resetButton = document.createElement('button');
const layout = document.createElement('div');
const tray = document.createElement('div');
const partGrid = document.createElement('div');
const caseArea = document.createElement('div');
const trayTitle = document.createElement('h4');
const caseTitle = document.createElement('h4');
const caseFrame = document.createElement('div');
const caseInterior = document.createElement('div');
const motherboardGhost = document.createElement('div');
const psuShroud = document.createElement('div');
const rearSlots = document.createElement('div');

styleElement.textContent = [
  '.pc-assembly-app{--pc-ink:#f4f7fb;--pc-muted:#aab7c7;--pc-line:#425265;--pc-panel:#111923;--pc-deep:#080d13;--pc-accent:#e7b84b;--pc-blue:#5db0ff;--pc-good:#55d68b;color:var(--pc-ink);background:#0d141d;border:1px solid #334154;border-radius:14px;padding:18px;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;box-shadow:0 12px 32px rgba(0,0,0,.28)}',
  '.pc-app-header{display:flex;justify-content:space-between;gap:18px;align-items:flex-end}.pc-title-group{max-width:62ch}.pc-title-group h3{font-size:1.35rem;letter-spacing:-.02em;margin:0 0 5px}.pc-title-group p{color:var(--pc-muted);line-height:1.45;margin:0}.pc-controls{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap}.pc-name-field{min-width:190px}.pc-name-field label{display:block;color:var(--pc-muted);font-size:.78rem;margin-bottom:5px}.pc-name-field input{width:100%;box-sizing:border-box;border:1px solid #53657a;border-radius:8px;background:#090f16;color:var(--pc-ink);padding:9px 10px}.pc-reset{min-height:40px;border:1px solid #68809a;border-radius:8px;background:#1a2633;color:var(--pc-ink);padding:8px 12px;font-weight:650;cursor:pointer}',
  '.pc-live-row{display:flex;justify-content:space-between;gap:14px;align-items:center;margin:16px 0 12px;padding:10px 12px;background:#151f2b;border:1px solid #35465a;border-radius:10px}.pc-status{margin:0;font-weight:720;color:#f6d889}.pc-progress{margin:0;color:#9ecfff;font-size:.9rem;white-space:nowrap}',
  '.pc-bench{display:grid;grid-template-columns:minmax(210px,.68fr) minmax(420px,1.7fr);gap:16px;align-items:stretch}.pc-tray,.pc-case-panel{min-width:0}.pc-panel-title{font-size:.88rem;color:#d9e2ed;margin:0 0 9px}.pc-part-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.pc-part-card{position:relative;min-height:104px;border:1px solid #3e5064;border-radius:10px;background:#151f2a;color:var(--pc-ink);padding:8px 6px 7px;cursor:grab;text-align:center;transition:transform 160ms ease-out,border-color 160ms ease-out,background 160ms ease-out}.pc-part-card:hover{transform:translateY(-2px);border-color:#7bbcff;background:#192838}.pc-part-card:focus-visible,.pc-slot:focus-visible,.pc-reset:focus-visible,.pc-name-field input:focus-visible{outline:3px solid #f2c65d;outline-offset:2px}.pc-part-card:active{cursor:grabbing}.pc-part-card[disabled]{cursor:not-allowed;transform:none}.pc-step{position:absolute;top:6px;left:7px;color:#99abc0;font-size:.67rem}.pc-part-label{display:block;margin-top:5px;font-size:.76rem;font-weight:700}.pc-part-shape{position:relative;display:block;margin:15px auto 0;background:#263848;border:2px solid #82a2bd;box-sizing:border-box;box-shadow:0 4px 10px rgba(0,0,0,.32)}',
  '.pc-part-shape--cpu{width:43px;height:43px;border-radius:5px;background:#b7a26d;border-color:#e1d29d;box-shadow:inset 0 0 0 8px #26313d,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--ram{width:18px;height:58px;border-radius:2px;background:#1c604c;border-color:#75b697;box-shadow:inset 0 -6px 0 #d8bd67,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--ssd{width:72px;height:22px;border-radius:3px;background:#215b48;border-color:#79ac97;box-shadow:inset -9px 0 0 #d7bd68,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--cooler{width:54px;height:54px;border-radius:50%;background:#162d3b;border:7px double #63a7c7}.pc-part-shape--cooler:after{content:"";position:absolute;width:12px;height:12px;border-radius:50%;background:#a9d8eb;left:50%;top:50%;transform:translate(-50%,-50%)}.pc-part-shape--motherboard{width:66px;height:59px;border-radius:4px;background:#17473f;border-color:#619288;box-shadow:inset 12px 10px 0 #20313a,inset -8px -11px 0 #20313a,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--psu{width:65px;height:49px;border-radius:4px;background:#272f38;border-color:#7d8995;box-shadow:inset 0 0 0 8px #151b22,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--gpu{width:82px;height:30px;border-radius:4px;background:#293844;border-color:#83a4ba;box-shadow:inset 9px 0 0 #1b252e,inset -15px 0 0 #1b252e,0 4px 10px rgba(0,0,0,.32)}.pc-part-shape--cables{width:57px;height:48px;border:6px double #6fa5d6;border-top-color:transparent;border-bottom-color:transparent;border-radius:50%;background:transparent;box-shadow:none}',
  '.pc-case{position:relative;min-height:430px;overflow:hidden;border:9px solid #38434e;border-radius:9px;background:#080d12;box-shadow:inset 0 0 0 2px #111923,0 10px 26px rgba(0,0,0,.35)}.pc-case:before{content:"PC CASE • SIDE PANEL REMOVED";position:absolute;left:14px;top:9px;color:#8d9bab;font-size:.64rem;letter-spacing:.08em;z-index:10}.pc-case-interior{position:absolute;inset:31px 13px 13px}.pc-board-ghost{position:absolute;left:15%;top:6%;width:63%;height:61%;box-sizing:border-box;background:#102c29;border:2px solid #2d5d57;border-radius:5px;box-shadow:inset 0 0 0 7px #0c201f}.pc-board-ghost:before,.pc-board-ghost:after{content:"";position:absolute;background:#28534e}.pc-board-ghost:before{left:11%;top:70%;width:72%;height:2px}.pc-board-ghost:after{left:72%;top:10%;width:2px;height:55%}.pc-psu-shroud{position:absolute;left:0;bottom:0;width:100%;height:22%;background:#121922;border-top:2px solid #303c49}.pc-rear-slots{position:absolute;left:2%;top:48%;width:10%;height:25%;border:1px solid #344252;box-shadow:inset 0 -6px 0 #1a2430,inset 0 -13px 0 #0a1017,inset 0 -20px 0 #1a2430,inset 0 -27px 0 #0a1017}.pc-fan{position:absolute;right:1.5%;width:13%;aspect-ratio:1;border:7px double #385f78;border-radius:50%;background:#111c26;box-sizing:border-box}.pc-fan:after{content:"";position:absolute;left:50%;top:50%;width:18%;height:18%;border-radius:50%;background:#6bbef0;transform:translate(-50%,-50%)}.pc-fan--one{top:4%}.pc-fan--two{top:31%}.pc-fan--three{top:58%}',
  '.pc-slot{position:absolute;box-sizing:border-box;border:2px dashed #65798d;border-radius:6px;background:rgba(20,31,42,.82);color:#d5e0eb;padding:4px;font-size:clamp(.55rem,1.15vw,.73rem);font-weight:720;line-height:1.1;cursor:pointer;display:flex;align-items:center;justify-content:center;text-align:center;transition:border-color 160ms ease-out,background 160ms ease-out,box-shadow 160ms ease-out,transform 160ms ease-out}.pc-slot:hover{border-style:solid;background:#1d3040}.pc-slot[data-kind="cpu"]{border-radius:5px}.pc-slot[data-kind="ram"]{border-radius:3px;writing-mode:vertical-rl}.pc-slot[data-kind="ssd"]{border-radius:3px}.pc-slot[data-kind="cooler"]{border-radius:50%;background:rgba(17,31,42,.65)}.pc-slot[data-kind="motherboard"]{align-items:flex-end;justify-content:flex-start;padding:8px;background:rgba(15,43,40,.48)}.pc-slot[data-kind="psu"]{background:rgba(35,43,52,.9)}.pc-slot[data-kind="gpu"]{background:rgba(31,44,55,.92)}.pc-slot[data-kind="cables"]{border-radius:18px;background:rgba(23,37,49,.88)}',
  '@media(max-width:760px){.pc-app-header{align-items:stretch;flex-direction:column}.pc-controls{align-items:stretch}.pc-name-field{flex:1}.pc-bench{grid-template-columns:1fr}.pc-part-grid{grid-template-columns:repeat(4,minmax(88px,1fr));overflow-x:auto;padding-bottom:5px}.pc-part-card{min-height:98px}.pc-case{min-height:390px}.pc-live-row{align-items:flex-start;flex-direction:column}.pc-progress{white-space:normal}}',
  '@media(max-width:480px){.pc-assembly-app{padding:12px}.pc-part-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.pc-case{min-height:340px;border-width:6px}.pc-slot{font-size:.52rem}}',
  '@media(prefers-reduced-motion:reduce){.pc-part-card,.pc-slot{transition:none}}'
].join('\\n');

heading.textContent = 'PC Assembly Bench';
directions.textContent = 'Build from the motherboard outward. Drag each shaped component to its matching location, or select a part and then its destination.';
nameLabel.textContent = 'Builder name';
nameLabel.htmlFor = 'pc-builder-name';
builderName.id = 'pc-builder-name';
builderName.type = 'text';
builderName.placeholder = 'Enter your name';
builderName.autocomplete = 'name';
resetButton.type = 'button';
resetButton.textContent = 'Reset build';
trayTitle.textContent = 'Parts tray';
caseTitle.textContent = 'Motherboard and case layout';
status.setAttribute('role', 'status');
status.setAttribute('aria-live', 'polite');

app.className = 'pc-assembly-app';
header.className = 'pc-app-header';
titleGroup.className = 'pc-title-group';
controls.className = 'pc-controls';
liveRow.className = 'pc-live-row';
status.className = 'pc-status';
progress.className = 'pc-progress';
resetButton.className = 'pc-reset';
layout.className = 'pc-bench';
tray.className = 'pc-tray';
partGrid.className = 'pc-part-grid';
caseArea.className = 'pc-case-panel';
trayTitle.className = 'pc-panel-title';
caseTitle.className = 'pc-panel-title';
caseFrame.className = 'pc-case';
caseInterior.className = 'pc-case-interior';
motherboardGhost.className = 'pc-board-ghost';
psuShroud.className = 'pc-psu-shroud';
rearSlots.className = 'pc-rear-slots';

const partCards = [];
const slotButtons = [];

function calculateAccuracy(results) {
  let correctAttempts = 0;
  for (const result of results) {
    if (result === true) {
      correctAttempts += 1;
    }
  }
  return Math.round((correctAttempts / results.length) * 100);
}

function checkPlacement(partIndex, slotIndex) {
  const correctPart = partIndex === currentStep;
  const correctSlot = slotIndex === currentStep;
  return correctPart && correctSlot;
}

function updateProgress() {
  const accuracy = attempts.length === 0 ? 100 : calculateAccuracy(attempts);
  progress.textContent = 'Installed ' + currentStep + ' of ' + parts.length + ' • Accuracy ' + accuracy + '%';
}

function updateStatus(message) {
  const nameInput = document.getElementById('pc-builder-name');
  const name = nameInput === null ? '' : nameInput.value.trim();
  status.textContent = name === '' ? message : name + ': ' + message;
}

function selectPart(index) {
  if (index < currentStep || partCards[index].disabled) {
    return;
  }
  selectedPart = index;
  partCards.forEach(function(card, cardIndex) {
    card.style.outline = cardIndex === index ? '3px solid #f2c65d' : 'none';
    card.setAttribute('aria-pressed', cardIndex === index ? 'true' : 'false');
  });
  updateStatus(parts[index].name + ' selected. Choose its destination.');
}

function updateTargetGuidance() {
  slotButtons.forEach(function(slotButton, index) {
    if (slotButton.disabled) {
      return;
    }
    const isNext = index === currentStep;
    slotButton.style.borderColor = isNext ? '#e7b84b' : '#65798d';
    slotButton.style.boxShadow = isNext ? '0 5px 18px rgba(231,184,75,.28)' : 'none';
    slotButton.setAttribute('aria-current', isNext ? 'step' : 'false');
  });
}

function placePart(partIndex, slotIndex) {
  const validPart = Number.isInteger(partIndex) && partIndex >= 0 && partIndex < parts.length;
  if (!validPart || partCards[partIndex].disabled) {
    updateStatus('Choose a part from the tray first.');
    return;
  }

  const isCorrect = checkPlacement(partIndex, slotIndex);
  attempts.push(isCorrect);

  if (isCorrect) {
    const installedPart = parts[partIndex];
    partCards[partIndex].disabled = true;
    partCards[partIndex].draggable = false;
    partCards[partIndex].style.opacity = '0.35';
    slotButtons[slotIndex].disabled = true;
    slotButtons[slotIndex].textContent = '✓ ' + installedPart.name;
    slotButtons[slotIndex].style.borderColor = '#55d68b';
    slotButtons[slotIndex].style.background = '#174a34';
    slotButtons[slotIndex].style.boxShadow = '0 5px 18px rgba(85,214,139,.22)';
    slotButtons[slotIndex].style.pointerEvents = 'none';
    currentStep += 1;
    updateStatus('Correct! ' + installedPart.name + ' snapped into place.');
  } else {
    const expected = parts[currentStep];
    updateStatus('Incorrect. ' + parts[partIndex].name + ' returned to the tray. Install ' + expected.name + ' in ' + expected.slot + ' next.');
  }

  selectedPart = -1;
  partCards.forEach(function(card) {
    card.style.outline = 'none';
    card.setAttribute('aria-pressed', 'false');
  });
  updateProgress();
  updateTargetGuidance();

  if (currentStep === parts.length) {
    updateStatus('PC assembly complete!');
  }
}

parts.forEach(function(part, index) {
  const partCard = document.createElement('button');
  const stepLabel = document.createElement('span');
  const partShape = document.createElement('span');
  const partLabel = document.createElement('span');
  partCard.type = 'button';
  partCard.className = 'pc-part-card';
  partCard.draggable = true;
  partCard.setAttribute('aria-label', 'PC part: ' + part.name);
  partCard.setAttribute('aria-pressed', 'false');
  partCard.setAttribute('data-part-index', String(index));
  stepLabel.className = 'pc-step';
  stepLabel.textContent = String(index + 1);
  partShape.className = 'pc-part-shape pc-part-shape--' + part.kind;
  partShape.setAttribute('aria-hidden', 'true');
  partLabel.className = 'pc-part-label';
  partLabel.textContent = part.name;
  partCard.appendChild(stepLabel);
  partCard.appendChild(partShape);
  partCard.appendChild(partLabel);
  partCard.addEventListener('click', function() {
    selectPart(index);
  });
  partCard.addEventListener('dragstart', function(event) {
    selectPart(index);
    event.dataTransfer.setData('text/plain', String(index));
    event.dataTransfer.effectAllowed = 'move';
  });
  partCards.push(partCard);
  partGrid.appendChild(partCard);

  const slotButton = document.createElement('button');
  slotButton.type = 'button';
  slotButton.textContent = part.slot;
  slotButton.className = 'pc-slot';
  slotButton.setAttribute('aria-label', 'Install a part in ' + part.slot);
  slotButton.setAttribute('data-kind', part.kind);
  slotButton.setAttribute('data-slot-index', String(index));
  slotButton.style.left = part.left + '%';
  slotButton.style.top = part.top + '%';
  slotButton.style.width = part.width + '%';
  slotButton.style.height = part.height + '%';
  slotButton.style.zIndex = String(part.layer);
  slotButton.addEventListener('click', function() {
    placePart(selectedPart, index);
  });
  slotButton.addEventListener('dragover', function(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  });
  slotButton.addEventListener('drop', function(event) {
    event.preventDefault();
    const droppedPart = Number.parseInt(event.dataTransfer.getData('text/plain'), 10);
    placePart(droppedPart, index);
  });
  slotButtons.push(slotButton);
});

resetButton.addEventListener('click', function() {
  attempts.length = 0;
  currentStep = 0;
  selectedPart = -1;
  partCards.forEach(function(card) {
    card.disabled = false;
    card.draggable = true;
    card.style.opacity = '1';
    card.style.outline = 'none';
    card.setAttribute('aria-pressed', 'false');
  });
  slotButtons.forEach(function(slotButton, index) {
    slotButton.disabled = false;
    slotButton.textContent = parts[index].slot;
    slotButton.style.borderColor = '#65798d';
    slotButton.style.background = '';
    slotButton.style.boxShadow = 'none';
    slotButton.style.pointerEvents = 'auto';
  });
  updateStatus('Next part: ' + parts[currentStep].name);
  updateProgress();
  updateTargetGuidance();
});

const nameField = document.createElement('div');
nameField.className = 'pc-name-field';
nameField.appendChild(nameLabel);
nameField.appendChild(builderName);
titleGroup.appendChild(heading);
titleGroup.appendChild(directions);
controls.appendChild(nameField);
controls.appendChild(resetButton);
header.appendChild(titleGroup);
header.appendChild(controls);
liveRow.appendChild(status);
liveRow.appendChild(progress);
tray.appendChild(trayTitle);
tray.appendChild(partGrid);
caseArea.appendChild(caseTitle);
caseInterior.appendChild(motherboardGhost);
caseInterior.appendChild(psuShroud);
caseInterior.appendChild(rearSlots);

['one', 'two', 'three'].forEach(function(position) {
  const fan = document.createElement('div');
  fan.className = 'pc-fan pc-fan--' + position;
  fan.setAttribute('aria-hidden', 'true');
  caseInterior.appendChild(fan);
});

slotButtons.forEach(function(slotButton) {
  caseInterior.appendChild(slotButton);
});
caseFrame.appendChild(caseInterior);
caseArea.appendChild(caseFrame);
layout.appendChild(tray);
layout.appendChild(caseArea);
app.appendChild(header);
app.appendChild(liveRow);
app.appendChild(layout);
outputElement.appendChild(styleElement);
outputElement.appendChild(app);

if (outputElement.clientWidth <= 480) {
  outputElement.style.minHeight = '1300px';
  outputElement.style.maxHeight = '1300px';
  outputElement.style.height = '1300px';
}

updateStatus('Next part: ' + parts[currentStep].name);
updateProgress();
updateTargetGuidance();
{% endcapture %}

{% include runners/ui.html
   runner_id="pc-javascript"
   challenge=pc_javascript_challenge
   code=pc_javascript_code
   height="1100px"
   output_height="780px"
%}

**Example output (initial UI state)**

```text
Next part: CPU
Installed 0 of 8 • Accuracy 100%
```

---

# Full Program Prototype

The full program uses the same lists, procedure, selection, iteration, Boolean logic, and accuracy calculation. It starts in Python, and the dropdown also provides complete Pseudocode and Java versions. The editable sample attempts supply input because this web runner does not provide terminal standard input.

{% capture pc_python_challenge %}
Run the automatic sample build. Then change the sample values to try a different assembly order.
{% endcapture %}

{% capture pc_python_code %}
parts = ["CPU", "RAM", "M.2 SSD", "CPU cooler", "Motherboard", "Power supply", "Graphics card", "Power cables"]
slots = ["CPU socket", "RAM slots", "M.2 slot", "Cooler mount", "Board tray", "PSU bay", "PCIe slot", "Power headers"]
attempts = []
current_step = 0

# Sample choices keep this example runnable in the web code runner.
# Change these lists to test a different build order.
sample_attempts = [
    ("Graphics card", "PCIe slot"),
    ("CPU", "CPU socket"),
    ("RAM", "RAM slots"),
    ("M.2 SSD", "M.2 slot"),
    ("CPU cooler", "Cooler mount"),
    ("Motherboard", "Board tray"),
    ("Power supply", "PSU bay"),
    ("Graphics card", "PCIe slot"),
    ("Power cables", "Power headers"),
]
sample_index = 0

def check_placement(part_name, slot_name):
    correct_part = part_name.lower() == parts[current_step].lower()
    correct_slot = slot_name.lower() == slots[current_step].lower()
    return correct_part and correct_slot

while current_step < len(parts):
    print("\nNext part:", parts[current_step])
    selected_part, selected_slot = sample_attempts[sample_index]
    print("Choose a PC part:", selected_part)
    print("Choose its destination:", selected_slot)
    is_correct = check_placement(selected_part, selected_slot)
    attempts.append(is_correct)
    sample_index += 1

    if is_correct:
        print(selected_part, "snapped into place!")
        current_step += 1
    else:
        print("Incorrect placement. The part returned to the tray.")
        print("Hint:", parts[current_step], "goes in", slots[current_step])

correct_attempts = 0
for result in attempts:
    if result:
        correct_attempts += 1

accuracy = round((correct_attempts / len(attempts)) * 100)
print("\nPC assembly complete!")
print("Accuracy:", str(accuracy) + "%")
{% endcapture %}

{% include runners/code.html
   runner_id="pc-python"
   language="python"
   variants_key="prototype"
   python_code=pc_python_code
   local_python=true
   challenge=pc_python_challenge
   code=pc_python_code
   height="760px"
%}

**Sample output**

```text
Next part: CPU
Choose a PC part: Graphics card
Choose its destination: PCIe slot
Incorrect placement. The part returned to the tray.
Hint: CPU goes in CPU socket

Next part: CPU
Choose a PC part: CPU
Choose its destination: CPU socket
CPU snapped into place!
... (remaining steps omitted) ...
PC assembly complete!
Accuracy: 89%
```

---

# Reflection

JavaScript felt most natural for this project because it connects directly to browser buttons, visible output, and the snap-in interaction. Python made the algorithm shorter and easier to read, but its normal `input()` and `print()` interface is text-based. Pseudocode was the clearest planning language because it showed the lists, procedure, selection, iteration, and Boolean logic without extra browser or terminal syntax.

The main difference is how each language handles interaction. JavaScript creates and updates HTML elements with event listeners. Python normally pauses for terminal input and prints a response. Both languages still use the same underlying algorithm and data.
