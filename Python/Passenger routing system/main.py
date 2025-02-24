import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import random
import matplotlib.pyplot as plt


def create_graph(cities):
    G = nx.DiGraph()
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                distance = random.randint(1, 10)
                cost = random.randint(5, 15)
                time = random.randint(10, 60)
                G.add_edge(cities[i], cities[j], weight=distance, cost=cost, time=time)
    return G


def dijkstra_path(G, source, target, weight):
    try:
        path = nx.dijkstra_path(G, source=source, target=target, weight=weight)
        length = nx.dijkstra_path_length(G, source=source, target=target, weight=weight)
        return path, length
    except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
        return None, None


def astar_path(G, source, target, heuristic):
    try:
        path = nx.astar_path(G, source=source, target=target, heuristic=heuristic)
        length = nx.astar_path_length(G, source=source, target=target, heuristic=heuristic)
        return path, length
    except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
        return None, None


def bfs_path(G, source, target):
    try:
        path = list(nx.shortest_path(G, source=source, target=target))
        length = len(path) - 1  # تعداد یال‌ها
        return path, length
    except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
        return None, None


def display_results(result_label, path, length, metric):
    if path:
        result_label.config(text=f"بهترین مسیر بر اساس {metric}:\n" + " -> ".join(path) + f"\nمجموع {metric}: {length}")
    else:
        result_label.config(text=f"مسیر مستقیمی برای {metric} بین مبدأ و مقصد وجود ندارد.")


def search_path():
    source = source_var.get()
    target = target_var.get()
    if source == target:
        messagebox.showerror("خطا", "مبدأ و مقصد نمی‌توانند یکسان باشند.")
        return

    # پیدا کردن بهترین مسیر بر اساس مسافت (Dijkstra)
    path_distance, length_distance = dijkstra_path(G, source, target, weight='weight')
    display_results(result_label_distance, path_distance, length_distance, 'مسافت')

    # پیدا کردن بهترین مسیر بر اساس هزینه (Dijkstra)
    path_cost, length_cost = dijkstra_path(G, source, target, weight='cost')
    display_results(result_label_cost, path_cost, length_cost, 'هزینه')

    # پیدا کردن بهترین مسیر بر اساس زمان سفر (A*)
    def heuristic(u, v):
        return 0  # برای مثال، می‌توان از تخمین فاصله استفاده کرد

    path_time, length_time = astar_path(G, source, target, heuristic=heuristic)
    display_results(result_label_time, path_time, length_time, 'زمان سفر')

    # پیدا کردن مسیر با کمترین تعداد یال‌ها (BFS)
    path_bfs, length_bfs = bfs_path(G, source, target)
    display_results(result_label_bfs, path_bfs, length_bfs, 'تعداد یال‌ها')

    # ترسیم نقشه نتایج
    draw_result_graph(G, path_distance, path_cost, path_time, path_bfs)


def draw_initial_graph(G):
    pos = nx.spring_layout(G, seed=42)  # ثابت نگه داشتن موقعیت‌ها برای رسم بهتر
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=12, font_color="black",
            font_weight="bold", edge_color="gray", linewidths=2)

    # اضافه کردن برچسب به یال‌ها
    edge_labels = nx.get_edge_attributes(G, 'weight')
    formatted_edge_labels = {k: f'{v} km' for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_size=10)

    plt.title("نقشه اولیه شهرها")
    plt.show()


def draw_result_graph(G, path_distance, path_cost, path_time, path_bfs):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(14, 10))

    # رسم گراف اصلی
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightgray", font_size=12, font_color="black",
            font_weight="bold", edge_color="gray", linewidths=2)

    # رسم مسیرها با خطوط و رنگ‌های متفاوت
    if path_distance:
        path_edges = list(zip(path_distance, path_distance[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3, label='مسافت', style='solid')

    if path_cost:
        path_edges = list(zip(path_cost, path_cost[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="blue", width=3, label='هزینه', style='dashed')

    if path_time:
        path_edges = list(zip(path_time, path_time[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="green", width=3, label='زمان سفر',
                               style='dotted')

    if path_bfs:
        path_edges = list(zip(path_bfs, path_bfs[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="purple", width=3, label='تعداد یال‌ها',
                               style='dashdot')

    # اضافه کردن برچسب‌ها به یال‌ها
    edge_labels_distance = nx.get_edge_attributes(G, 'weight')
    formatted_edge_labels_distance = {k: f'{v} km' for k, v in edge_labels_distance.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels_distance, font_color='red', font_size=10)

    edge_labels_cost = nx.get_edge_attributes(G, 'cost')
    formatted_edge_labels_cost = {k: f'{v} $' for k, v in edge_labels_cost.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels_cost, font_color='blue', font_size=10)

    edge_labels_time = nx.get_edge_attributes(G, 'time')
    formatted_edge_labels_time = {k: f'{v} min' for k, v in edge_labels_time.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels_time, font_color='green', font_size=10)

    plt.legend(["مسافت", "هزینه", "زمان سفر", "تعداد یال‌ها"], loc="upper left")
    plt.title("گراف شهرها و مسیرهای مختلف")
    plt.show()


# لیست شهرها
cities = ['همدان', 'تهران', 'تبریز', 'اصفهان', 'مشهد', 'کردستان', 'گیلان', 'ارومیه']

# ساخت گراف کامل
G = create_graph(cities)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("سیستم مسیریابی مسافران")

# ایجاد و تنظیم لیست‌های کشویی برای مبدأ و مقصد
source_var = tk.StringVar()
target_var = tk.StringVar()

ttk.Label(root, text="شهر مبدأ:").grid(column=0, row=0, padx=10, pady=10)
source_menu = ttk.Combobox(root, textvariable=source_var, values=cities, state="readonly")
source_menu.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="شهر مقصد:").grid(column=0, row=1, padx=10, pady=10)
target_menu = ttk.Combobox(root, textvariable=target_var, values=cities, state="readonly")
target_menu.grid(column=1, row=1, padx=10, pady=10)

# دکمه جستجو
search_button = ttk.Button(root, text="جستجوی مسیر", command=search_path)
search_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# برچسب‌های نمایش نتایج
result_label_distance = ttk.Label(root, text="")
result_label_distance.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

result_label_cost = ttk.Label(root, text="")
result_label_cost.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

result_label_time = ttk.Label(root, text="")
result_label_time.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

result_label_bfs = ttk.Label(root, text="")
result_label_bfs.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# ترسیم گراف اولیه
draw_initial_graph(G)

# اجرای برنامه
root.mainloop()
