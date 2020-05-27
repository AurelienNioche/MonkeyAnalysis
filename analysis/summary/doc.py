from parameters.parameters import SAME_X, SAME_P, SIG_STEEP, SIG_MID

DOC = {
    "risk_aversion": "Best-fit parameter value "
                     "describing the risk aversion",
    "distortion": "Best-fit parameter value "
                  "describing the probability distortion",
    "precision": "Best-fit parameter value "
                 "describing the precision",
    SAME_P: "Median of the frequencies with which "
                 "the monkey chooses the best target "
                 "for a specific alternative "
                 "such that: "
                 "(i) a best option exists, "
                 "(ii) probabilities of non-zero outputs are the same, "
                 "(iii) the non-zero outputs are different "
                 "(iv) the possible outputs are only zero and positive rewards",
    SAME_X: "Median of the frequencies with which "
                  "the monkey chooses the best target "
                  "for a specific alternative "
                  "such that: "
                  "(i) a best option exists, "
                  "(ii) probabilities of non-zero outputs are different, "
                  "(iii) the non-zero outputs are the same "
                  "(iv) the possible outputs are only zero and positive rewards",
    SIG_STEEP: "Best-fit parameter value for the steepness of the curve for the 'same p - gain vs loss' control trials",
    SIG_MID: "Best-fit parameter value for the midpoint of the curve for the 'same p - gain vs loss'control trials",
}