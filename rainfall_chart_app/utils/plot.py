import json
import plotly
import pandas as pd
import plotly.express as px


def create_plot_data(file_path):
	"""
		Creates plot data from the given file
	"""

	df = pd.read_excel(file_path)
	df.sort_values(by=['time'], ascending=True)
	df['time'] = pd.to_datetime(df['time'], format='%m/%d/%Y %H:%M')
	df['RG_A'] = df['RG_A'].fillna(0).astype(int)
	
	# Resample the data as the x-axis can't hold much data points.
	df_daily = df.resample('D', on='time').mean().reset_index()
	df_daily['RG_A_smooth'] = df_daily['RG_A'].rolling(window=7).mean()

	df['month_year'] = df['time'].dt.strftime('%B %Y')
	month_year_list = df['month_year'].unique()
	duration = f"from {month_year_list[0]} to {month_year_list[-1]}" if len(month_year_list) > 1 else f"for {month_year_list[0]}"

	fig = px.line(df_daily, x='time', y='RG_A_smooth', title=f'Average Rainfall Record in Birmingham {duration}', markers=True,
				labels={'RG_A_smooth': 'Millimeters'}, template='plotly_white')

	fig.update_traces(line=dict(width=2))
	fig.update_layout(xaxis_title='Time', yaxis_title='Millimeters', 
					legend_title_text='Legend', 
					hovermode='x unified')

	graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graph_json
