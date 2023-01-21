from datetime import date;
import pandas as pd;

initial_investemnt = 25;
yearly_staking_reward = 0.1;
pitch_staking_reward = 0.08;
start_date = date(2019, 4, 15);
pitch_date = date(2020, 4, 15);
end_date = date(2021, 4, 15);
reward_payment_day = 23;
reinvest_staking_reward = True;

start_investment_amount = 25;
pitch_investment_amount = 0;
reward_amount = 0;
total_reward_amount_to_date = 0;


# obtaining start position
first_reward_date_check = date(
    int(str(start_date).split("-")[0]), 
    int(str(start_date).split("-")[1]),
    reward_payment_day);

if (first_reward_date_check > start_date):
    first_reward_date = first_reward_date_check;
else:
    splitted = str(first_reward_date_check).split("-");
    if(first_reward_date_check.month < 12):
        first_reward_date = date(
            int(splitted[0]),
            int(splitted[1])+1,
            int(splitted[2])
        );
    else:
        first_reward_date = date(
            int(splitted[0])+1,
            1,
            int(str(first_reward_date_check).split("-")[2])
        );


# increment date by one month
def add_month(datee):
    date_splitter = str(datee).split("-");
    if (int(date_splitter[1]) < 12):
        year = int(date_splitter[0]);
        month = int(date_splitter[1])+1;
        day = int(date_splitter[2]);
        datee = date(year, month, day);
    else:
        year = int(date_splitter[0])+1;
        month = 1;
        day = int(date_splitter[2]);
        datee = date(year, month, day);
    return datee;


# calculating data
# first date
days = (first_reward_date - start_date).days;
reward_date_list = [first_reward_date];
reward_amount_list = [yearly_staking_reward * start_investment_amount * days / 365]; # actual / 365
total_reward_amount_to_date_list = [reward_amount_list[0]];
investment_amount_list = [start_investment_amount];
staking_reward_rate_list = [str(int(yearly_staking_reward*100))+".00%"];
line_list = [1];
i=0;

# middle dates
while (reward_date_list[i] < pitch_date):

    reward_date = add_month(reward_date_list[i]);
    reward_date_list.append(reward_date);

    investment_amount = investment_amount_list[i] + reward_amount_list[i];
    investment_amount_list.append(investment_amount);

    days = (reward_date_list[i+1] - reward_date_list[i]).days;
    reward_amount = yearly_staking_reward * investment_amount_list[i+1] * days / 365; # actual / 365
    reward_amount_list.append(reward_amount);

    total_reward_amount_to_date = total_reward_amount_to_date_list[i] + reward_amount_list[i+1];
    total_reward_amount_to_date_list.append(total_reward_amount_to_date);

    staking_reward_rate_list.append(staking_reward_rate_list[i]);
    line_list.append(line_list[i]+1);
    i+=1;

reward_date_list.pop(-1);
reward_amount_list.pop(-1);
investment_amount_list.pop(-1);
total_reward_amount_to_date_list.pop(-1);
staking_reward_rate_list.pop(-1);
line_list.pop(-1);

i-=1;
while (reward_date_list[i] < end_date):
    reward_date = add_month(reward_date_list[i]);
    reward_date_list.append(reward_date);

    investment_amount = investment_amount_list[i] + reward_amount_list[i];
    investment_amount_list.append(investment_amount);

    days = (reward_date_list[i+1] - reward_date_list[i]).days;
    reward_amount = pitch_staking_reward * investment_amount_list[i+1] * days / 365; # actual / 365
    reward_amount_list.append(reward_amount);

    total_reward_amount_to_date = total_reward_amount_to_date_list[i] + reward_amount_list[i+1];
    total_reward_amount_to_date_list.append(total_reward_amount_to_date);

    staking_reward_rate_list.append(str(int(pitch_staking_reward*100))+".00%");
    line_list.append(line_list[i]+1);
    i+=1;

reward_date_list.pop(-1);
reward_amount_list.pop(-1);
investment_amount_list.pop(-1);
total_reward_amount_to_date_list.pop(-1);
staking_reward_rate_list.pop(-1);
line_list.pop(-1);

# ending date
days = (end_date - reward_date_list[-1]).days;
reward_date_list.append(end_date);
investment_amount_list.append(investment_amount_list[-1] + reward_amount_list[-1]);
reward_amount_list.append(pitch_staking_reward * investment_amount_list[-1] * days / 365); # actual / 365
total_reward_amount_to_date_list.append(reward_amount_list[-1]+total_reward_amount_to_date_list[-1]);
staking_reward_rate_list.append(str(int(pitch_staking_reward*100))+".00%");
line_list.append(line_list[-1]+1);


# rounding to 6 decimals
investment_amount_list = [format(i, '.6f') for i in investment_amount_list];
reward_amount_list = [format(i, '.6f') for i in reward_amount_list];
total_reward_amount_to_date_list = [format(i, '.6f') for i in total_reward_amount_to_date_list];

# creating dictionary for dataframe
data_for_frame = {
    "Line #": line_list,
    "Reward Date": reward_date_list,
    "Investment Amount": investment_amount_list,
    "Reward Amount": reward_amount_list,
    "Total Reward Amount To Date": total_reward_amount_to_date_list,
    "Staking Reward Rate": staking_reward_rate_list
}; 


# data frame export to csv
eth = pd.DataFrame(data_for_frame);
eth.to_csv("bonus_task1.csv", index=False);