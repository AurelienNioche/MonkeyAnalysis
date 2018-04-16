from model import parameter_estimate
import plot.utility
import plot.precision
import plot.probability_distortion


def main():

    fig_folder = "fig"
    r = parameter_estimate.run()

    for monkey in "Havane", "Gladys":

        plot.utility.plot(fig_name=f"{fig_folder}/utility_{monkey}.pdf",
                          positive_risk_aversion=r[monkey]["pos_risk_aversion"],
                          negative_risk_aversion=r[monkey]["neg_risk_aversion"])

        plot.probability_distortion.plot(fig_name=f"{fig_folder}/distortion_{monkey}.pdf")
        plot.precision.plot()


if __name__ == "__main__":

    main()

