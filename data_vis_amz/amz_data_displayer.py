#!/usr/bin/env python3

"""
This is a Data Visualization project. This script takes in a .csv file
and turns the data into charts in order to better interpret the trends.
"""

#import pyexcel
from datetime import date
import pandas as pd
import matplotlib
#Use Agg for high quality png files and raster images, PDF for vector images in pdf
matplotlib.use('Agg')
import csv
import numpy as np
import itertools

#creat graphs
import matplotlib.pyplot as plt

#data has 12 columns


def device_type_graph(data):
    print('mobile/desktop')

    N = 2 #(number of options in device column)
    selected_data = data['Device Type Group'].iloc[:].values
    #print(selected_data)
    mobile = 0 
    desktop = 0 
    for device in selected_data:
        if device == 'PHONE':
            mobile+=1
        else:
            desktop+=1
    print(f"Mobile count: {mobile} Desktop count: {desktop}")
    ind = np.arange(N)

    p1 = plt.bar(ind, mobile)
    # stack p2 on top of p1
    p2 = plt.bar(ind, desktop)

    plt.ylabel("Sales converted on Amazon")
    plt.title("Device Used")
    plt.xticks(ind, ("Mobile", "Desktop"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[1]), ("Mobile", "Desktop"))
    plt.savefig("device_graph.png")


def device_day_per_week_graph():
    print('device distribution per day graph')


def category_pie_chart(data):
    print('pie chart')
    selected_data = data['Category'].iloc[:].values
    categories = {}
    for category in selected_data:
        if category not in categories:
            categories[f'{category}'] = 1
        else:
            categories[f'{category}'] += 1 
    
    print (categories)
    labels = categories.keys()
    #make size based on the number of categories

    sizes = categories.values()

    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('category_pie_chart.png')

def week1_week2_line_chart(data):
    print('week1 vs week2 lines')
    dates = data['Date Shipped'].iloc[:].values
    prices = data['Price($)'].iloc[:].values
    #prices = pd.to_datetime(prices)
    #print(prices)
    no_of_items = data['Items Shipped'].iloc[:].values
    
    week1 = {}
    week2 = {}
    for (date, price) in zip(dates, prices):
        print(type(date))
        if "6/1/2021" in date:
            week1['1'] += float(price)
        elif "6/2/2021" in date:
            week1['2'] += float(price)
        elif "6/3/2021" in date:
            week1['3'] += float(price)
        elif "6/4/2021" in date:
            week1['4'] += float(price)
        elif "6/5/2021" in date:
            week1['5'] += float(price)
        elif "6/6/2021" in date:
            week1['6'] += float(price)
        elif "6/7/2021" in date:
            week1['7'] += float(price)
        elif "6/8/2021" in date:
            week2['8'] += float(price)
        elif "6/9/2021" in date:
            week2['9'] += float(price)
        elif "6/10/2021" in date:
            week2['10'] += float(price)
        elif "6/11/2021" in date:
            week2['11'] += float(price)
        elif "6/12/2021" in date:
            week2['12'] += float(price)
        elif "6/13/2021" in date:
            week2['13'] += float(price)
        elif "6/14/2021" in date:
            week2['14'] += float(price)
        else:
            break

    

    plt.plot(week1)
    plt.plot(week2)
    plt.legend(["blue", "green"], loc='lower right')
    plt.savefig('week1_vs_week2.png')


def category_revenue():
    print('category revenue')
    np.random.seed(19680801)
    #n equal to number of categories
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.savefig('category_revenue.png')









#make graphs that have a height that adjusts for the max value being passed in

def main ():
    csv_file = 'Amz_Aff_Data6_1-14.csv'
    Affiliate_Data = pd.read_csv(csv_file, encoding='utf-8')
    print('main works')
    #csv_interpreter(csv_file)
    # category_revenue()
    device_type_graph(Affiliate_Data)
    # device_day_per_week_graph()
    category_pie_chart(Affiliate_Data)
    week1_week2_line_chart(Affiliate_Data)
    
    # plt.ioff()
    # plt.plot([1.6, 2.7])
    # plt.show()

    #save the file locally .png
    #plt.savefig("firstgraph.png")


if __name__ == '__main__':
    main()
