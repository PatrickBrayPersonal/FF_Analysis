import pandas as pd

def main():
    ff_data = import_data()
    ff_data = clean_data(ff_data)
    ff_data = points_per_team(ff_data)

def import_data():
    raw_df = pd.read_csv("C:/Users/patri/OneDrive/Fantasy Football/weekly/2019/week1.csv")
    for i in range(2,18):
        raw_df = raw_df.merge(pd.read_csv("C:/Users/patri/OneDrive/Fantasy Football/weekly/2019/week" + str(i) + ".csv"), on = 'Player', how = 'outer')
    return raw_df

def clean_data(ff_data):
    halfPPRColumns = ['week1.HalfPPRFantasyPoints',
    'week2.HalfPPRFantasyPoints', 'week3.HalfPPRFantasyPoints',
    'week4.HalfPPRFantasyPoints', 'week5.HalfPPRFantasyPoints',
    'week6.HalfPPRFantasyPoints', 'week7.HalfPPRFantasyPoints',
    'week8.HalfPPRFantasyPoints', 'week9.HalfPPRFantasyPoints',
    'week10.HalfPPRFantasyPoints', 'week11.HalfPPRFantasyPoints',
    'week12.HalfPPRFantasyPoints', 'week13.HalfPPRFantasyPoints',
    'week14.HalfPPRFantasyPoints', 'week15.HalfPPRFantasyPoints',
    'week16.HalfPPRFantasyPoints', 'week17.HalfPPRFantasyPoints']
    ff_data[halfPPRColumns] = ff_data[halfPPRColumns].astype(float)
    ff_data['HalfPPRFantasyPoints2019'] = ff_data.iloc[:, -17:-1].sum(axis=1)

    return ff_data



def points_per_team(ff_data):
    points_col = ff_data.groupby(['Tm'])['HalfPPRFantasyPoints2019'].sum()
    points_col = points_col.orderby
    print(points_col)
    return points_col
    

main()