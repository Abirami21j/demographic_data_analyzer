import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # race count
    race_count = df['race'].value_counts()

    # average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # percentage with Bachelors
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # advanced education
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # rich with advanced education
    higher_edu_rich = round(
        (df[higher_edu]['salary'] == '>50K').sum() /
        len(df[higher_edu]) * 100, 1)

    # rich without advanced education
    lower_edu_rich = round(
        (df[~higher_edu]['salary'] == '>50K').sum() /
        len(df[~higher_edu]) * 100, 1)

    # min hours
    min_work_hours = df['hours-per-week'].min()

    # rich percentage among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() /
        len(num_min_workers) * 100, 1)

    # country with highest rich percentage
    country_salary = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts() / df['native-country'].value_counts() * 100
    )
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1)

    # top occupation in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') &
           (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
