from marketing_generator.brochure import create_brochure

def main():
    uw = "https://www.washington.edu/datasciencemasters/"
    ut = "https://cdso.utexas.edu/msds"
    uc = "https://codas.uchicago.edu/academics/ms-data-science/"

    uw_brochure = create_brochure("University of Washington MSDS", uw)
    ut_brochure = create_brochure("University of Texas MSDS Online", ut)
    uc_brochure = create_brochure("University of Chicago MSDS", uc)

    print("\n=== UW Brochure ===\n", uw_brochure)
    print("\n=== UT Brochure ===\n", ut_brochure)
    print("\n=== UChicago Brochure ===\n", uc_brochure)

    # Optionally persist to files for the ranking script to read
    with open("uw_brochure.md", "w") as f:
        f.write(uw_brochure)
    with open("ut_brochure.md", "w") as f:
        f.write(ut_brochure)
    with open("uc_brochure.md", "w") as f:
        f.write(uc_brochure)

if __name__ == "__main__":
    main()
