# CODE_RUNNER: 3.06 Homework - Message scoring and advice
def score_message(message, amount_requested, known_contact):
    risk_score = 0
    # No else is needed: an absent signal contributes zero to the existing score.
    if "gift cards" in message.lower():
        risk_score = risk_score + 4
    # No else is needed: amounts at or below 100 leave the score unchanged.
    if amount_requested > 100:
        risk_score = risk_score + 3
    # No else is needed: a known sender contributes zero, not a negative score.
    if not known_contact:
        risk_score = risk_score + 2
    return risk_score

def report_risk(risk_score):
    # 3 thresholds -> 4 outcomes -> 4 answers
    if risk_score >= 9:
        print("Do not reply. This is almost certainly a scam.")
    elif risk_score >= 6:
        print("This looks risky. Check with someone you trust before replying.")
    elif risk_score >= 3:
        print("Be a little careful, but this is probably fine.")
    else:
        print("Nothing suspicious in this message.")

message = "URGENT: send gift cards now to unlock your account"
amount_requested = 500
known_contact = False
risk_score = score_message(message, amount_requested, known_contact)
print("Risk score:", risk_score)
report_risk(risk_score)
