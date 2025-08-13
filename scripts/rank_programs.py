from marketing_generator.evaluate import rank_brochures

def main():
    # If you saved outputs in run_brochures.py:
    with open("ut_brochure.md") as f:
        ut_brochure = f.read()
    with open("uc_brochure.md") as f:
        uc_brochure = f.read()
    with open("uw_brochure.md") as f:
        uw_brochure = f.read()

    ranking = rank_brochures(ut_brochure, uc_brochure, uw_brochure)
    print("\n=== Ranking ===\n", ranking)

if __name__ == "__main__":
    main()
