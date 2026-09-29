function lunchPlan(lunchPacked, practiceAfterSchool) {
  if (lunchPacked) {
    if (practiceAfterSchool) {
      return "Bring packed lunch and an extra practice snack.";
    } else {
      return "Bring packed lunch; no practice snack needed.";
    }
  } else {
    if (practiceAfterSchool) {
      return "Buy lunch and an extra practice snack.";
    } else {
      return "Buy lunch; no practice snack needed.";
    }
  }
}
for (const packed of [true, false]) {
  for (const practice of [true, false]) {
    console.log(lunchPlan(packed, practice));
  }
}
