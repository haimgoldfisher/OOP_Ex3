import pandas as pd
import matplotlib.pyplot as plt


def load_save_A():
    df = pd.read_csv("../csv/load_save_A.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Load & Save")
    # plt.savefig("load_save_a")
    plt.show()


def load_save():
    df = pd.read_csv("../csv/load_save.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Load & Save")
    # plt.savefig("load_save")
    plt.show()


def center_A():
    df = pd.read_csv("../csv/center_A.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Center")
    # plt.savefig("center_a")
    plt.show()


def center():
    df = pd.read_csv("../csv/center.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Center")
    # plt.savefig("center")
    plt.show()


def shortest_path_A():
    df = pd.read_csv("../csv/shortest_path_A.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Shortest Path")
    # plt.savefig("shortest_path_a")
    plt.show()


def shortest_path():
    df = pd.read_csv("../csv/shortest_path.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="Shortest Path")
    # plt.savefig("shortest_path")
    plt.show()


def tps_A():
    df = pd.read_csv("../csv/tps_A.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="TPS")
    # plt.savefig("tps_a")
    plt.show()


def tps():
    df = pd.read_csv("../csv/tps.csv", index_col=0)
    df = df.transpose()
    df.plot(marker="o", ylabel="Time (in Seconds)", xlabel="Graphs", figsize=(10, 6), fontsize=13, title="TPS")
    # plt.savefig("tps")
    plt.show()


def finished():
    data = {'Java': 39, 'Python': 45}
    colors = ['orange', 'blue']
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(6, 5))
    plt.bar(courses, values, color=colors,width=0.3)
    plt.xlabel("Languages")
    plt.ylabel("# of finished algos")
    plt.title("Number of Functions / Algorithms completed")
    # plt.savefig("comp")
    plt.show()


if __name__ == '__main__':

    load_save_A()
    shortest_path_A()
    center_A()
    tps_A()

    load_save()
    shortest_path()
    center()
    tps()
    finished()