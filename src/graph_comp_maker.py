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


if __name__ == '__main__':
    load_save_A()
    shortest_path_A()
    center_A()
    tps_A()

    load_save()
    shortest_path()
    center()
    tps()