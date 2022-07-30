from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as sql

'''PANDAS SECTION'''

teams_of_ipl = pd.read_csv("Teams of ipl.csv")
most_runs = pd.read_csv("Runs maker.csv")
wicket_takers = pd.read_csv("Wicket takers.csv")
most_sixes = pd.read_csv("Most sixes.csv")
most_hatricks = pd.read_csv("Most hatricks.csv")
single_acheivement = pd.read_csv("Single achivement.csv")
individual_record = pd.read_csv("Individual record.csv")

'''GUI SECTION'''

gui = Tk()
gui.title('IPL DATA ANALYSIS PROJECT')
gui.geometry('500x500') # width x height
gui.minsize(1530, 810) # width , height
gui.maxsize(2000, 1500) # width , height



# Heading frame

frame_head = Frame(gui, bg="blue", borderwidth=9, relief=SUNKEN)
frame_head.pack(fill="x")

label_head = Label(frame_head, text="TATA IPL DATA ANALYSIS", font="Algerian 25 italic", bg="blue", fg="white")
label_head.pack(pady=3)

# Footer frame

frame_foot = Frame(gui, bg="blue", borderwidth=9, relief=SUNKEN)
frame_foot.pack(side='bottom', fill="x")

quit_button = Button(frame_foot, text='QUIT PROGRAM', command=gui.destroy, bg="lightskyblue1", fg="black",
                     font="Calibri 12 italic", borderwidth=5, relief=RAISED)
quit_button.pack(pady=3)

# Bottom frame

frame_bottom = Frame(gui, bg="lightblue3", borderwidth=7, relief=RIDGE)
frame_bottom.pack(side='bottom', fill="y")

# Left side UP frame

frame_left_up = Frame(gui, bg="black", borderwidth=7, relief=RIDGE)
frame_left_up.pack(fill=Y, side=LEFT)

# Workspace frame

frame_workspace = Frame(gui, bg="lightblue2", borderwidth=7, relief=RIDGE)
canvas_b_workspace = Canvas(frame_workspace, width=1125, height=480, scrollregion=(0, 0, 500, 500))

frame_workspace.pack(anchor=NE, fill="both")

work_label = Label(frame_workspace, text="Workspace", bg="lightblue2", fg="blue", font="Algerian 25 italic")
work_label.pack()

# bottom frame labels textbox and buttons

label1 = Label(frame_bottom, text="ADD DETAILS", bg="lightblue3", font="Aparajita 15 bold")
label1.grid(row=1, column=1, pady=1.5)

label2 = Label(frame_bottom, text="FIND DATA USING NAME", bg="lightblue3", font="Aparajita 15 bold")
label2.grid(row=2, column=1, pady=1.5, padx=2)

label3 = Label(frame_bottom, text="RESULT", bg="lightblue3", font="Aparajita 15 bold")
label3.grid(row=3, column=1, pady=2)

label4 = Label(frame_bottom, text="NAME", bg="lightblue3", font="Aparajita 15 bold")
label4.grid(row=0, column=2, pady=1.5)

label5 = Label(frame_bottom, text="ROLL", bg="lightblue3", font="Aparajita 15 bold")
label5.grid(row=0, column=3, pady=1.5)

label6 = Label(frame_bottom, text="TEAM", bg="lightblue3", font="Aparajita 15 bold")
label6.grid(row=0, column=4, pady=1.5)

label7 = Label(frame_bottom, text="MATCHES PLAYED", bg="lightblue3", font="Aparajita 15 bold")
label7.grid(row=0, column=5, pady=1.5)

label8 = Label(frame_bottom, text="RUNS & WICKETS", bg="lightblue3", font="Aparajita 15 bold")
label8.grid(row=0, column=6, pady=1.5)

'''ADD details'''
name_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
team_entry = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
matches_played_entry = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")
runs_wicket_entry = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")

name_entry.grid(row=1, column=2, padx=2)
roll_entry.grid(row=1, column=3, padx=2)
team_entry.grid(row=1, column=4, padx=2)
matches_played_entry.grid(row=1, column=5, padx=2)
runs_wicket_entry.grid(row=1, column=6, padx=2)

'''Find data'''
name_entry2 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry2 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")

name_entry2.grid(row=2, column=2, padx=2)
roll_entry2.grid(row=2, column=3, padx=2)

'''RESULT'''
name_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
roll_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
team_entry3 = Entry(frame_bottom, textvariable=StringVar, font="Abadi 15 italic")
matches_played_entry3 = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")
runs_wicket_entry3 = Entry(frame_bottom, textvariable=IntVar, font="Abadi 15 italic")

name_entry3.grid(row=3, column=2, padx=2, pady=2.5)
roll_entry3.grid(row=3, column=3, padx=2, pady=2.5)
team_entry3.grid(row=3, column=4, padx=2, pady=2.5)
matches_played_entry3.grid(row=3, column=5, padx=2, pady=2.5)
runs_wicket_entry3.grid(row=3, column=6, padx=2, pady=2.5)

# Function

# Function used in bottom frame
def add():
    mysql_connection = sql.connect(host='localhost', user='root', passwd='123456789', database="crickters_data")

    player = name_entry.get()
    roll = roll_entry.get()
    team = team_entry.get()
    matches = matches_played_entry.get()
    runs_wicket = runs_wicket_entry.get()

    cur = mysql_connection.cursor()
    query = f"insert into player_data values('{player}','{team}','{roll}',{matches},{runs_wicket});"
    cur.execute(query)
    mysql_connection.commit()
    mysql_connection.close()

    messagebox.showinfo('INFO', 'DATA ADDED TO DATABASE')

    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    team_entry.delete(0, END)
    matches_played_entry.delete(0, END)
    runs_wicket_entry.delete(0, END)

    mysql_connection.close()

def search():

    # clear all result column
    name_entry3.delete(0, END)
    roll_entry3.delete(0, END)
    team_entry3.delete(0, END)
    matches_played_entry3.delete(0, END)
    runs_wicket_entry.delete(0, END)
    mysql_connection = sql.connect(host='localhost', user='root', passwd='123456789', database="crickters_data")

    # getting enter data
    name = name_entry2.get()
    roll = roll_entry2.get()

    # sql query
    df = pd.read_sql(f"select * from Player_data where PLAYER='{name}' and ROLL='{roll}';", mysql_connection)

    # inserting data from database
    Team = df.iloc[:, 1:2]
    Matches = df.iloc[:, 3:4]
    R_W = df.iloc[:, 4:]

    name_entry3.insert(0, name)
    roll_entry3.insert(0, roll)
    team_entry3.insert(0, Team)
    matches_played_entry3.insert(0, Matches)
    runs_wicket_entry3.insert(0, R_W)

    messagebox.showinfo('INFO', 'Data matches to Dataframe')


    mysql_connection.close()

# Functions used for graph
def g1():
    team = list(teams_of_ipl['Abbreviation'])
    won = list(teams_of_ipl['Won'])
    lost = list(teams_of_ipl['Lost'])

    plt.bar(team, won, 0.15, label='WON')
    plt.bar(np.arange(len(team)) + 0.15, lost, 0.15, label='LOST')

    plt.xlabel('Names of team')
    plt.legend()

    plt.show()

def g2():
    team = list(teams_of_ipl['Abbreviation'])
    won = list(teams_of_ipl['Win %'])

    plt.pie(won, labels=team)

    plt.show()

def g3():
    player = list(most_runs['Player Name'])
    matches = list(most_runs['Matches'])
    hc = list(most_runs['50s'])
    c = list(most_runs['100s'])

    plt.bar(player, matches, 0.15, label='MATCHES PLAYED')
    plt.bar(np.arange(len(player)) + 0.15, hc, 0.15, label='HALF CENTURIES')
    plt.bar(np.arange(len(player)) + 0.30, c, 0.15, label='CENTURIES')

    plt.legend()
    plt.xlabel('Player name')

    plt.show()

def g4():
    player = list(most_hatricks['PLAYER'])
    hatricks = list(most_hatricks['NO. of HATRICKS IN IPL'])

    plt.barh(player, hatricks, color='green')

    plt.ylabel('Player name')
    plt.xlabel('Hatricks')

    plt.show()

def g5():
    top10 = most_sixes.head(10)

    player = list(top10['PLAYER'])
    sixes = list(top10['6s'])
    matches = list(top10['Matches'])

    plt.barh(player, sixes, 0.5, color='green')
    plt.barh(np.arange(len(player)) + 0.35, matches, 0.5, color='yellow')

    plt.ylabel('Player name')
    plt.xlabel('Sixes in number of Matches')

    plt.show()

def g6():
    team = list(teams_of_ipl['Abbreviation'])
    titles = list(teams_of_ipl['Titles'])
    exp = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    plt.pie(titles, labels=team, explode=exp, autopct='%3d%%')

    plt.show()

# Function used for creating table structure
def table(df):
    table_df = Table(canvas_b_workspace, dataframe=df, width=900, height=430)
    table_df.show()

# Functions used in buttons
def B1_workspace():

    canvas_b_workspace.pack(pady=5)

    table(teams_of_ipl)

def B2_workspace():

    canvas_b_workspace.pack(pady=5)

    table(most_runs)

def B3_workspace():

    canvas_b_workspace.pack(pady=5)

    table(wicket_takers)

def B4_workspace():

    canvas_b_workspace.pack(pady=5)

    table(most_sixes)

def B5_workspace():

    canvas_b_workspace.pack(pady=5)

    table(most_hatricks)

def B6_workspace():

    canvas_b_workspace.pack(pady=5)

    table(single_acheivement)

def B7_workspace():

    canvas_b_workspace.pack(pady=5)

    table(individual_record)

def BG_charts():
    graph = Tk()
    graph.title('CHARTS AND GRAPHS')
    graph.geometry('340x360')
    graph.maxsize(340, 360)

    frame_graph = Frame(graph, bg="black", borderwidth=7, relief=RIDGE)
    frame_graph.pack(fill=X)

    b1 = Button(frame_graph, text="               Matches Won Lost             ", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g1)
    b1.pack(pady=5)

    b2 = Button(frame_graph, text="              WIN% OF TEAMS               ", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g2)
    b2.pack(pady=5)

    b4 = Button(frame_graph, text="      HATRICKS BY TOP PLAYER      ", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g4)
    b4.pack(pady=5)

    b3 = Button(frame_graph, text="HALF CENTURIES AND CENTURIES\nBY TOP PLAYER", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g3)
    b3.pack(pady=5)

    b5 = Button(frame_graph, text="        MOST SIXES BY PLAYER        \nIN MATCHES", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g5)
    b5.pack(pady=5)

    b6 = Button(frame_graph, text="          THE CHAMPION TEAM          ", font="Cavolini 13 italic",
                borderwidth=5, relief=RAISED, bg="yellow", fg="green", command=g6)
    b6.pack(pady=5)

    graph.mainloop()


# Buttons of ADD and SEARCH

button_add = Button(frame_bottom, text="   ADD    ", font="Cavolini 13 italic", borderwidth=5, relief=RAISED,
                    bg="lightblue1", command=add)
button_add.grid(row=1, column=7, padx=40)

button_search = Button(frame_bottom, text="SEARCH", font="Cavolini 13 italic", borderwidth=5, relief=RAISED,
                       bg="lightblue1", command=search)
button_search.grid(row=2, column=7, padx=40, pady=3)

# Buttons of left side

button_1 = Button(frame_left_up, text="                   Teams of IPL                 ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B1_workspace)
button_2 = Button(frame_left_up, text="           MOST RUNS SCORED         ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B2_workspace)
button_3 = Button(frame_left_up, text="          MOST WICKET TAKERS       ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B3_workspace)
button_4 = Button(frame_left_up, text="        MOST SIXES BY PLAYER        ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B4_workspace)
button_5 = Button(frame_left_up, text="               MOST HATRICKS             ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B5_workspace)
button_6 = Button(frame_left_up, text="SINGLE ACHIEVEMENTS RECORD", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B6_workspace)
button_7 = Button(frame_left_up, text="          INDIVIDUAL RECORDS        ", font="Cavolini 13 italic",
                  borderwidth=5, relief=RAISED, bg="yellow1", command=B7_workspace)
button_graph = Button(frame_left_up, text="           GRAPHS & CHARTS            ", font="Cavolini 13 italic",
                      borderwidth=5, relief=RAISED,  bg="yellow1", command=BG_charts)

button_1.pack(pady=6, padx=8)
button_2.pack(pady=6, padx=8)
button_3.pack(pady=6, padx=8)
button_4.pack(pady=6, padx=8)
button_5.pack(pady=6, padx=8)
button_6.pack(pady=6, padx=8)
button_7.pack(pady=6, padx=8)
button_graph.pack(pady=6, padx=8)

# Left side Bottom frame

frame_left_down = Frame(frame_left_up, bg="black", borderwidth=7, relief=RIDGE)
frame_left_down.pack(fill=Y)

log_label = Label(frame_left_down, text="LOG DATA", bg="black", fg="green",
                  font="Aparajita 17 bold")
log_label.pack()

log_label1 = Label(frame_left_down, text="WRITE EVERYTHING IN CAPITAL LETTER", bg="black", fg="green",
                   font="Aparajita 12 bold")
log_label1.pack(padx=43)

gui.mainloop()

print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('|| **        **     **     * * *    * * * *           *            **       * * *    ||')
print('|| * *      * *    *  *    *    *   *          ********* *        *  *     *     *   ||')
print('|| *  *    *  *   * ** *   *     *  * * * *    *********** *     * ** *   *          ||')
print('|| *   *  *   *  *      *  *    *   *          ********* *      *      *  *    * *   ||')
print('|| *    **    * *        * * * *    * * * *           *        *        *  * * *  *  ||')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')

input('press any key to exit')

