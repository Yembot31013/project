import matplotlib.pyplot as plt
import numpy as np

#dynamic

class BarProcess:
  def __init__(self, labels: list[str], boy_means: list[int], girl_means: list[int], ylabel: str, title: str, flabel: str, slabel: str):
    self.labels = labels #["wednesday", "Thursday", "Friday"]
    self.boy_means = boy_means #[20, 34, 27]
    self.girl_means = girl_means #[28, 31, 22]
    self.ylabel = ylabel #"Total Number"
    self.title = title #"CIH statistics"
    self.flabel = flabel #"boy"
    self.slabel = slabel #"girl"

    x = np.arange(len(self.labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, self.boy_means, width, label=self.flabel)
    rects2 = ax.bar(x + width/2, self.girl_means, width, label=self.slabel)

    ax.set_ylabel(self.ylabel)
    ax.set_title(self.title)
    ax.set_xticks(x, self.labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

  def save(self, file):
    plt.savefig(file)

  def show(self):
    plt.show()

class PieProcess:
  def __init__(self, data: list[float], label: list[str], title: str, heading:str):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw = dict(aspect="equal"))
    self.data = data #["wednesday", "Thursday", "Friday"]
    self.label = label #[20, 34, 27]
    self.title = title #CIH statistics
    self.heading = heading #Total Number

    wedges, texts, autotexts = ax.pie(self.data, autopct=lambda pct: self.func(pct, data), textprops=dict(color="w"))

    ax.legend(wedges, self.label, title=self.title, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(self.heading)

  def func(self, pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)
    
  def show(self):
    plt.show()

if __name__ == "__main__":
  
  labels = ["wednesday", "Thursday", "Friday"]
  boy_means = [20, 34, 27]
  girl_means = [28, 31, 22]
  ylabel = "Total Number"
  title = "CIH statistics"
  flabel = "boy"
  slabel = "girl"

  process = PieProcess(boy_means, labels, ylabel, title)

  process.show()