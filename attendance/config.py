import pandas as pd
import matplotlib.pyplot as plt

# Defaults for matplot lib
plt.rcParams["figure.figsize"] = (10, 7)


# Load and clean the data. For how the cleaning is done, see the cleaning notebook.
survey = pd.read_csv('/workspaces/snowmass-attendance/clean_survey.csv')

# # Convert the time colunm to a time
# raw_survey["time"] = pd.to_datetime(raw_survey.Timestamp)

# # Rename columns to be easy to access in code
# survey = raw_survey.rename(columns={
#     "I'm employed by": "employed_by",
# })
# # c_Timestamp = "TimeStamp"
# # c_attend = 1,
# # c_attend_text = 2
# # c_dinner = "If you attended the conference, would you also attend the dinner?"
# # c_worried_about = "Please indicate how worried you are about each issue that might prevent you from attending: [COVID],Please indicate how worried you are about each issue that might prevent you from attending: [Funding],Please indicate how worried you are about each issue that might prevent you from attending: [Length of the Workshop],Please indicate how worried you are about each issue that might prevent you from attending: [Accessibility/Accommodation],Please indicate how worried you are about each issue that might prevent you from attending: [Competing Responsibilities]"
# # c_worried_about_why = "If there are other issues that concern you that are not listed above, please indicate here!"
# # c_hearing_acc = "Is there any type of hearing-related accommodation that would increase the accessibility of the Snowmass Summer Study for you? (Please note that captioning can be useful for both Deaf and hard of hearing people and for people who do not have these identities but who find it helpful to be able to see as well as hear speakers' words.)"
# # c_accomodations = "What other accommodations would increase the accessibility of the Snowmass Summer Study for you?"
# # c_accomodations_text = "Do you have any additional details you'd like to share or any other comments on how Snowmass Summer Study accessibility could be improved for you?"
# # c_covid = "The points below are labeled on the case/day plot above. Please indicate the largest USA new case-load/day rate for which you'd be willing to attend Snowmass in person."
# # c_covid_text = "There is no way to get everyone's full perspective with a multiple choice question like that. Please feel free to add a sentence or so if you wish!"
# # c_frontier = "I primarily am interested in sessions associated with:"
# # c_rank = "I am a"
# # c_travel = "If I attend Snowmass, I will be traveling"
# # c_management = "Are you part of the Snowmass Management Team (frontier group or sub-group convener, etc.)?"
