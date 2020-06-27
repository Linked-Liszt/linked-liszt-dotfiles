def compare_samples(var_0_list, var_1_list):

    print(f"{len(var_0_list)} samples loaded into variable 0")
    print(f"{len(var_1_list)} samples loaded into variable 1")
    print("------------------------------------")

    # Begin F Test
    print("Beginning F Test")
    print("------------------------------------")
    mean_var_0 = np.mean(var_0_list)
    mean_var_1 = np.mean(var_1_list)
    print(f"mean var 0: {mean_var_0}")
    print(f"mean var 1: {mean_var_1}")
    f = np.var(var_0_list)/np.var(var_1_list)
    print(f"F: {f}")
    f_crit = sps.f.cdf(f, len(var_0_list) - 1, len(var_1_list) - 1)
    print(f"F critical: {f_crit}")
    print("------------------------------------")

    # Are variances equal?
    print("Are variances equal?")
    print("------------------------------------")
    print("is mean(var 0) > mean(var 2) and F < F critical?")
    print("or is mean(var 0) < mean(var 2) and F > F critical? ")
    print("------------------------------------")
    var_equal = (mean_var_0 > mean_var_1) and (f < f_crit)
    var_equal = var_equal or ((mean_var_0 < mean_var_1) and (f > f_crit))
    if var_equal:
        print("Variances are Equal")
    else:
        print("Variances are Unequal")
    print("------------------------------------")

    if var_equal:
        print("Begin two-tailed two-sample t-test assuming equal variances")
    else:
        print("Begin two-tailed two-sample t-test assuming unequal variances")
    t_t_test, p_t_test = sps.ttest_ind(var_0_list, var_1_list, equal_var=var_equal)
    print(f"T-Test Value: {t_t_test}")
    print(f"Two tailed p: {p_t_test}")
    print("------------------------------------")
    print("Assuming alpha=0.05")
    print("------------------------------------")
    if p_t_test > 0.05:
        print("Null Hypothesis Accepted, Algorithm is NOT statistically better")
    else:
        print("Null Hypothesis Rejected, Algorithm is statistically better")