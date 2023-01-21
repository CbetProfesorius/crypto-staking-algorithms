import tkinter as tk;
import pandas as pd;
from datetime import date;

gui = tk.Tk();
gui.title("Task 3");
gui.configure(bg="light blue");
gui.geometry("650x450");

lb1 = tk.Label(gui, text="Initial Investment Amount (e.g. 10): ", padx=30, pady=5);
lb1.grid(row=0, column=0, sticky=tk.W);
lb1.config(bg="light blue");
investment_amount = tk.Entry(gui);
investment_amount.grid(row=0, column=1);

lb2 = tk.Label(gui, text="Yearly Staking Reward in % (e.g. 7): ", padx=30, pady=5);
lb2.grid(row=1, column=0, sticky=tk.W);
lb2.config(bg="light blue");
yearly_staking_reward = tk.Entry(gui);
yearly_staking_reward.grid(row=1, column=1);

lb3 = tk.Label(gui, text="Start Date (e.g. 2020-11-10): ", padx=30, pady=5);
lb3.grid(row=2, column=0, sticky=tk.W);
lb3.config(bg="light blue");
start_date = tk.Entry(gui);
start_date.grid(row=2, column=1);

lb4 = tk.Label(gui, text="End Date (e.g. 2022-11-10): ", padx=30, pady=5);
lb4.grid(row=3, column=0, sticky=tk.W);
lb4.config(bg="light blue");
end_date = tk.Entry(gui);
end_date.grid(row=3, column=1);

lb5 = tk.Label(gui, text="Reward Payment Day (e.g. 15): ", padx=30, pady=5);
lb5.grid(row=4, column=0, sticky=tk.W);
lb5.config(bg="light blue");
reward_payment_day = tk.Entry(gui);
reward_payment_day.grid(row=4, column=1);

lb6 = tk.Label(gui, text="Reinvest Staking Reward (yes/no): ", padx=30, pady=5);
lb6.grid(row=5, column=0, sticky=tk.W);
lb6.config(bg="light blue");
reinvest_staking_reward = tk.Entry(gui);
reinvest_staking_reward.grid(row=5, column=1);

lb7 = tk.Label(gui, text="Output file name (e.g. output_data): ", padx=30, pady=5);
lb7.grid(row=6, column=0, sticky=tk.W);
lb7.config(bg="light blue");
output_file = tk.Entry(gui);
output_file.grid(row=6, column=1);

lb8 = tk.Label(gui);
lb8.grid(row=7);
lb8.config(bg="light blue");

lb9 = tk.Label(gui, text="Yearly Staking Reward Change in % (e.g. 5): ", padx=30, pady=5);
lb9.grid(row=8, column=0, sticky=tk.W);
lb9.config(bg="light blue");
pitch_staking_reward = tk.Entry(gui);
pitch_staking_reward.grid(row=8, column=1);
pitch_staking_reward.insert(0, "Empty if not changed");
pitch_staking_reward.config(fg="grey");
pitch_staking_reward.bind("<FocusIn>", lambda event: pitch_staking_reward.delete(0, "end") if pitch_staking_reward.get() == "Empty if not changed" else None);
pitch_staking_reward.bind("<FocusOut>", lambda event: pitch_staking_reward.insert(0, "Empty if not changed") if pitch_staking_reward.get() == "" else None);

lb10 = tk.Label(gui, text="Date of Change (e.g. 2021-11-10): ", padx=30, pady=5);
lb10.grid(row=9, column=0, sticky=tk.W);
lb10.config(bg="light blue");
pitch_date = tk.Entry(gui);
pitch_date.grid(row=9, column=1);
pitch_date.insert(0, "Empty if not changed");
pitch_date.config(fg="grey");
pitch_date.bind("<FocusIn>", lambda event: pitch_date.delete(0, "end") if pitch_date.get() == "Empty if not changed" else None);
pitch_date.bind("<FocusOut>", lambda event: pitch_date.insert(0, "Empty if not changed") if pitch_date.get() == "" else None);
tk.Label(gui).grid(row=10);

# object
class Currency:
    def __init__(self, investment_amount: float, yearly_staking_reward: float, start_date: date, end_date: date, reward_payment_day: int, reinvest_staking_reward: bool, output_file: str) -> None:
        self._investment_amount = investment_amount;
        self._yearly_staking_reward = yearly_staking_reward;
        self._start_date = start_date;
        self._end_date = end_date;
        self._reward_payment_day = reward_payment_day;
        self._reinvest_staking_reward = reinvest_staking_reward;
        self._output_file = output_file;
        self._pitch_staking_reward = None;
        self._pitch_date = None;

    @property
    def getInvestmentAmount(self) -> float:
        return self._investment_amount;
    
    @property
    def getYearlyStakingReward(self) -> float:
        return self._yearly_staking_reward;
    
    @property
    def getStartDate(self) -> date:
        return self._start_date;
    
    @property
    def getEndDate(self) -> date:
        return self._end_date;

    @property
    def getRewardPaymentDay(self) -> int:
        return self._reward_payment_day;

    @property
    def getReinvestStakingReward(self) -> bool:
        return self._reinvest_staking_reward;

    @property
    def getOutputFile(self) -> str:
        return self._output_file;

    @property
    def getPitchStakingReward(self) -> float:
        return self._pitch_staking_reward;

    @getPitchStakingReward.setter
    def setPitchStakingReward(self, pitch_staking_reward: float):
        self._pitch_staking_reward = pitch_staking_reward;

    @property
    def getPitchDate(self) -> date:
        return self._pitch_date;
    
    @getPitchDate.setter
    def setPitchDate(self, pitch_date: date):
        self._pitch_date = pitch_date;
 
# obtaining start position
def start_position(start_date, reward_payment_day) -> date:
    first_reward_date_check = date(
        int(str(start_date).split("-")[0]), 
        int(str(start_date).split("-")[1]),
        reward_payment_day
        );
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
    return first_reward_date;

# increment date by one month
def add_month(datee) -> date:
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
def calculation(currency: Currency):
    investment_amount = currency.getInvestmentAmount;
    yearly_staking_reward = currency.getYearlyStakingReward;
    start_date = currency.getStartDate;
    end_date = currency.getEndDate;
    reward_payment_day =  currency.getRewardPaymentDay;
    reinvest_staking_reward =  currency.getReinvestStakingReward;
    first_reward_date = start_position(start_date, reward_payment_day);
    if isinstance(currency.getPitchStakingReward, float):
        pitch_staking_reward =  currency.getPitchStakingReward;
        pitch_date =  currency.getPitchDate;
        if (reinvest_staking_reward):
            # first date
            days = (first_reward_date - start_date).days;
            reward_date_list = [first_reward_date];
            reward_amount_list = [yearly_staking_reward * investment_amount * days / 365]; # actual / 365
            total_reward_amount_to_date_list = [reward_amount_list[0]];
            investment_amount_list = [investment_amount];
            staking_reward_rate_list = [str(int(yearly_staking_reward*100))+".00%"];
            line_list = [1];
            i=0;
            # middle dates
            while (reward_date_list[i] < pitch_date):
                reward_date = add_month(reward_date_list[i]);
                reward_date_list.append(reward_date)
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
            investment_amount_list = [format(i, '.6f') for i in investment_amount_list];
            reward_amount_list = [format(i, '.6f') for i in reward_amount_list];
            total_reward_amount_to_date_list = [format(i, '.6f') for i in total_reward_amount_to_date_list];
        else:
            # first date
            days = (first_reward_date - start_date).days;
            reward_date_list = [first_reward_date];
            reward_amount_list = [yearly_staking_reward * investment_amount * days / 365]; # actual / 365
            total_reward_amount_to_date_list = [reward_amount_list[0]];
            investment_amount_list = [investment_amount];
            staking_reward_rate_list = [str(int(yearly_staking_reward*100))+".00%"];
            line_list = [1];
            i=0;
            # middle dates
            while (reward_date_list[i] < pitch_date):
                reward_date = add_month(reward_date_list[i]);
                reward_date_list.append(reward_date)
                investment_amount = investment_amount_list[i];
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
                investment_amount = investment_amount_list[i];
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
            investment_amount_list.append(investment_amount_list[-1]);
            reward_amount_list.append(pitch_staking_reward * investment_amount_list[-1] * days / 365); # actual / 365
            total_reward_amount_to_date_list.append(reward_amount_list[-1]+total_reward_amount_to_date_list[-1]);
            staking_reward_rate_list.append(str(int(pitch_staking_reward*100))+".00%");
            line_list.append(line_list[-1]+1);
            investment_amount_list = [format(i, '.6f') for i in investment_amount_list];
            reward_amount_list = [format(i, '.6f') for i in reward_amount_list];
            total_reward_amount_to_date_list = [format(i, '.6f') for i in total_reward_amount_to_date_list]
        return line_list, reward_date_list, investment_amount_list, reward_amount_list, total_reward_amount_to_date_list, staking_reward_rate_list;
    else:
        print("No Staking Reward Change Selected");
        if (reinvest_staking_reward):
            # first date
            days = (first_reward_date - start_date).days;
            reward_date_list = [first_reward_date];
            reward_amount_list = [yearly_staking_reward * investment_amount * days / 365]; # actual / 365
            total_reward_amount_to_date_list = [reward_amount_list[0]];
            investment_amount_list = [investment_amount];
            staking_reward_rate_list = [str(int(yearly_staking_reward*100))+".00%"];
            line_list = [1];
            i=0;
            # middle dates
            while (reward_date_list[i] < end_date):
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
            # ending date
            days = (end_date - reward_date_list[-1]).days;
            reward_date_list.append(end_date);
            investment_amount_list.append(investment_amount_list[-1] + reward_amount_list[-1]);
            reward_amount_list.append(yearly_staking_reward * investment_amount_list[-1] * days / 365); # actual / 365
            total_reward_amount_to_date_list.append(reward_amount_list[-1]+total_reward_amount_to_date_list[-1]);
            staking_reward_rate_list.append(str(int(yearly_staking_reward*100))+".00%");
            line_list.append(line_list[-1]+1);
            investment_amount_list = [format(i, '.6f') for i in investment_amount_list];
            reward_amount_list = [format(i, '.6f') for i in reward_amount_list];
            total_reward_amount_to_date_list = [format(i, '.6f') for i in total_reward_amount_to_date_list];
        else:
            # first date
            days = (first_reward_date - start_date).days;
            reward_date_list = [first_reward_date];
            reward_amount_list = [yearly_staking_reward * investment_amount * days / 365]; # actual / 365
            total_reward_amount_to_date_list = [reward_amount_list[0]];
            investment_amount_list = [investment_amount];
            staking_reward_rate_list = [str(int(yearly_staking_reward*100))+".00%"];
            line_list = [1];
            i=0;
            # middle dates
            while (reward_date_list[i] < end_date):
                reward_date = add_month(reward_date_list[i]);
                reward_date_list.append(reward_date);
                investment_amount = investment_amount_list[i];
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
            # ending date
            days = (end_date - reward_date_list[-1]).days;
            reward_date_list.append(end_date);
            investment_amount_list.append(investment_amount_list[-1]);
            reward_amount_list.append(yearly_staking_reward * investment_amount_list[-1] * days / 365); # actual / 365
            total_reward_amount_to_date_list.append(reward_amount_list[-1]+total_reward_amount_to_date_list[-1]);
            staking_reward_rate_list.append(str(int(yearly_staking_reward*100))+".00%");
            line_list.append(line_list[-1]+1);
            investment_amount_list = [format(i, '.6f') for i in investment_amount_list];
            reward_amount_list = [format(i, '.6f') for i in reward_amount_list];
            total_reward_amount_to_date_list = [format(i, '.6f') for i in total_reward_amount_to_date_list];
        return line_list, reward_date_list, investment_amount_list, reward_amount_list, total_reward_amount_to_date_list, staking_reward_rate_list

def frame(line_list, reward_date_list, investment_amount_list, reward_amount_list, total_reward_amount_to_date_list, staking_reward_rate_list):
    data_for_frame = {
        "Line #": line_list,
        "Reward Date": reward_date_list,
        "Investment Amount": investment_amount_list,
        "Reward Amount": reward_amount_list,
        "Total Reward Amount To Date": total_reward_amount_to_date_list,
        "Staking Reward Rate": staking_reward_rate_list
    };
    df = pd.DataFrame(data_for_frame);
    return df; 

def gui_result():
    # saving currency as object
    currency = Currency(
        float(investment_amount.get()),
        float(yearly_staking_reward.get())/100,
        date(int(str(start_date.get().split("-")[0])), int(str(start_date.get().split("-")[1])), int(str(start_date.get().split("-")[2]))),
        date(int(str(end_date.get().split("-")[0])), int(str(end_date.get().split("-")[1])), int(str(end_date.get().split("-")[2]))),
        int(reward_payment_day.get()),
        True if reinvest_staking_reward.get()=="yes" else False,
        str(output_file.get())
    );
    # checking staking reward change
    if ((pitch_staking_reward.get() is not None) and (pitch_staking_reward.get()!="Empty if not changed") and (pitch_staking_reward.get()!="")):
        currency.setPitchStakingReward = float(pitch_staking_reward.get())/100;
    if ((pitch_date.get() is not None) and (pitch_date.get()!="Empty if not changed") and (pitch_date.get()!="")):
        currency.setPitchDate = date(int(str(pitch_date.get().split("-")[0])), int(str(pitch_date.get().split("-")[1])), int(str(pitch_date.get().split("-")[2])));

    line_list, reward_date_list, investment_amount_list, reward_amount_list, total_reward_amount_to_date_list, staking_reward_rate_list = calculation(currency);
    df = frame(line_list, reward_date_list, investment_amount_list, reward_amount_list, total_reward_amount_to_date_list, staking_reward_rate_list);
    df.to_csv(f"{currency.getOutputFile}.csv", index=False);
    print("Generated Successfully!");


btn = tk.Button(gui, text="Generate", bg="orange", padx=10, pady=10, command=gui_result);
btn.grid(row=11, column=0, sticky=tk.E);

gui.mainloop();