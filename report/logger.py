from report.scorer import results, compute_score

def print_report():
    print("\n🚀 IRC EVALUATION REPORT\n")

    for section, data in results.items():
        status = data["status"]
        reason = data["reason"]

        if status == "PASS":
            print(f"[{section}] ✅ PASS")
        elif status == "FAIL":
            print(f"[{section}] ❌ FAIL")
        else:
            print(f"[{section}] ⚠️ PARTIAL")

        if reason:
            print(f"→ {reason}")

        print()

    print("--------------------------------")

    print(f"🏁 FINAL SCORE: {compute_score()} / 40\n")

    print("💬 EVALUATOR QUESTIONS:")

    for section, data in results.items():
        if data["status"] != "PASS":
            suggest_question(section)