#importing libraries
import pandas as pd
import numpy as np

#reading CSVs to DFs
df1=pd.read_csv("Katha_Accelerometer.csv",sep=",")
df2=pd.read_csv("Rosa_Accelerometer.csv", sep=",")
df3=pd.read_csv("Maja_Accelerometer.csv", sep=",")
df4=pd.read_csv("Peter_Accelerometer.csv", sep=",")

#adding new empty column "exercise" to define ground truth
df1['exercise'] = np.nan
df2['exercise'] = np.nan
df3['exercise'] = np.nan
df4['exercise'] = np.nan

#adding values into exercise of DFs
df1.loc[0:3032, "exercise"]="jumpingjacks"
df1.loc[3033:3632, "exercise"]="transition"
df1.loc[3633:6632, "exercise"]="plank"
df1.loc[6633:7232, "exercise"]="transition"
df1.loc[7233:10232, "exercise"]="situp"
df1.loc[10233:10832, "exercise"]="transition"
df1.loc[10833:13832, "exercise"]="squats"
df1.loc[13833:14435, "exercise"]="transition"

df2.loc[0:3124, "exercise"]="jumpingjacks"
df2.loc[3125:3749, "exercise"]="transition"
df2.loc[3750:6874, "exercise"]="plank"
df2.loc[6875:7499, "exercise"]="transition"
df2.loc[7500:10624, "exercise"]="situp"
df2.loc[10625:11249, "exercise"]="transition"
df2.loc[11250:14373, "exercise"]="squats"
df2.loc[14374:15040, "exercise"]="transition"

df3.loc[0:3124, "exercise"]="jumpingjacks"
df3.loc[3125:3749, "exercise"]="transition"
df3.loc[3750:6874, "exercise"]="plank"
df3.loc[6875:7499, "exercise"]="transition"
df3.loc[7500:10624, "exercise"]="situp"
df3.loc[10625:11249, "exercise"]="transition"
df3.loc[11250:14374, "exercise"]="squats"
df3.loc[14375:14538, "exercise"]="transition"

df4.loc[0:3032, "exercise"]="jumpingjacks"
df4.loc[3033:3632, "exercise"]="transition"
df4.loc[3633:6632, "exercise"]="plank"
df4.loc[6633:7232, "exercise"]="transition"
df4.loc[7233:10232, "exercise"]="situp"
df4.loc[10233:10832, "exercise"]="transition"
df4.loc[10833:13832, "exercise"]="squats"
df4.loc[13833:14591, "exercise"]="transition"

#keeping time series consecutive over all individual recordings
df2["Time (s)"] = df2["Time (s)"]+240.039
df3["Time (s)"] = df3["Time (s)"]+480.704
df4["Time (s)"] = df4["Time (s)"]+713.322

#concatenating DFs 1 to 4
frames = [df1, df2, df3, df4]
df = pd.concat(frames)

#renaming df columns
df = df.rename(columns={"Time (s)":"time", "Acceleration x (m/s^2)":"acc_x","Acceleration y (m/s^2)":"acc_y", "Acceleration z (m/s^2)":"acc_z"})

#define window size for running mean/std here once
window_size=100

#running avg/std
df['acc_x_mov_avg']=df['acc_x'].rolling(window_size).mean()
df['acc_y_mov_avg']=df['acc_y'].rolling(window_size).mean()
df['acc_z_mov_avg']=df['acc_z'].rolling(window_size).mean()
df['acc_x_mov_std']=df['acc_x'].rolling(window_size).std()
df['acc_y_mov_std']=df['acc_y'].rolling(window_size).std()
df['acc_z_mov_std']=df['acc_z'].rolling(window_size).std()

#plotting example
#df.plot(x='time', y='acc_x_mov_avg')

#rearrange order of columns (exercise at the end)
df = df[['time', 'acc_x', 'acc_y', 'acc_z', 'acc_x_mov_avg', 'acc_y_mov_avg', 'acc_z_mov_avg', 'acc_x_mov_std', 'acc_y_mov_std', 'acc_z_mov_std', 'exercise']]

#writing combined DF to .csv
df.to_csv("dataset_prepared.csv", index=False)
