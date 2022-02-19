from datetime import datetime as dt
import dash
from dash.exceptions import PreventUpdate

from dash_extensions import Download
from dash_extensions.snippets import send_file
# pip install dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

import plotly.express as px

import pandas as pd
import pathlib
import dash_auth




PATH = pathlib.Path(__file__)
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("order.csv"))
df1 = pd.read_csv(DATA_PATH.joinpath("order_detailes.csv"))



df['order_date'] = pd.to_datetime(df['order_date'])
df['month_year'] = pd.DatetimeIndex(df['order_date']).month
df['order_date'] = pd.to_datetime(df['order_date'])
df.set_index('order_date', inplace=True)

print(df.head())

v_frame=pd.DataFrame(
    {
       "order_source": ["Saler", "Customer", "Percentage"]  * 4,
       "sales": [1000,2000,3000,4000] * 3,
       "year":[2013,2014]* 6

     }
 )

#print(df.head())
df2 = pd.DataFrame(
    {
       "order id": [1, 2, 3, 4] * 3,
       "number of v": ["A", "B", "C"] * 4

     }
 )
 


# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],)

server = app.server
#auth = dash_auth.BasicAuth(
 #   app,
  #  {'roaa': '0000',
   #  }
#)

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

])


index_page = html.Div([


        html.Div([

    html.H1("Business Performance Management System", style = {'fontWeight': 'bold', 'color': 'white', 'textAlign': 'center'}),

        ]),
    html.Div([
        dbc.Nav(
            [

                dbc.NavLink(
            "Get Started",active=True, href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),
            ],
            pills=True,

        ),
            #className="me-1",style={'text-decoration':'none'}),
        #dbc.NavLink("Get Started", href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),


        html.Div(
dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active=True, href="/page-3")),
        dbc.NavItem(dbc.NavLink("Operational Level", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Stratgic Level", href="/page-2")),
        dbc.NavItem(dbc.NavLink("About",  href="page-4")),
        dbc.NavItem(dbc.NavLink("Help",  href="#", id="btn")),Download(id="download")
    ],
    pills=True,


        )
        )],
        className="navbar"),



       html.Div(
    [








    ],

),html.Br(),




    html.Div([


            html.Img(src=app.get_asset_url('startup1.jpg'))
            #html.Video(src="https://archive.org/download/WebmVp8Vorbis/webmvp8.webm")
            #html.A(src="https://www.youtube.com/watch?v=b-M2KQ6_bM4")



#changes
    ]),
    html.Footer([
        html.Div("Created By UofK Students © 2021 For Research Purpose"),

        html.Div([
            html.P(['Find Us On: '], id='find-me-on'),
            html.A([html.Img(src=app.get_asset_url('linkedInLogo.png'), style={'height': '2rem'})],
                   href="#"),
            html.A([html.Img(src=app.get_asset_url('facebookLogo.png'), style={'height': '2rem'})],
                   href="#")
        ], id='footer-links'),

    ],id='footer'),



html.Div([

       # html.Button('LOGOUT', id='btn2', n_clicks=0,style={'background-color': 'orange',
        #                                               'color': 'white',
         #                                              'text-decoration': 'none',
          #                                             'display': 'inline-block',
           #                                                'fontWeight': 'bold'
            #                                           }),
        html.Div(id='container')
])


])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
       return send_file("./assets/Manual.pdf")




page_1_layout =html.Div([
    html.Div([
        dbc.Nav(
            [

                dbc.NavLink(
            "Get Started",active=True, href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),
            ],
            pills=True,

        ),
            #className="me-1",style={'text-decoration':'none'}),
        #dbc.NavLink("Get Started", href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),


        html.Div(
dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/page-3")),
        dbc.NavItem(dbc.NavLink("Operational Level",active=True, href="/page-1")),
        dbc.NavItem(dbc.NavLink("Stratgic Level", href="/page-2")),
        dbc.NavItem(dbc.NavLink("About",  href="page-4")),
        dbc.NavItem(dbc.NavLink("Help",  href="#", id="btn")),Download(id="download")
    ],
    pills=True,


        )
        )],
        className="navbar"),
    html.Br(),

    
    html.H1("Operational Dashboard", style={'textAlign': 'center','color': 'white'}),
    

          html.Br(),
         

   
    html.Div(
        html.Div([
            html.P("Choose The channel/s Of Distribution For Your Products",style={'color': 'white','fontWeight': 'bold'}),
  dcc.Dropdown(id='Type', multi=True,
                     options=[{'label': x, 'value': x} for x in sorted(df.order_source.unique())],
               value=["client", "saler", "percent"]),
                      html.Br(),


       dcc.DatePickerRange(
        id='my-date-picker-range',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2014, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2021, 12, 30),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt.date(dt.now()),  # the month initially presented when the user opens the calendar
        start_date=dt(2014, 1, 1),
        end_date=dt.date(dt.now()),
        display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
        month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=2,  # minimum number of days between start and end date

        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  # session, local, or memory. Default is 'local'

        updatemode='singledate' , # singledate or bothdates. Determines when callback is triggered
        
       # style={'background': '#fff', 'cursor': 'pointer', 'padding': '5px 10px', 'border': '1px solid #ccc','width': '100%'}
    ),
    ],), ),
html.Div(id="output-div"),

    


],className="row flex-display" ,

    style={"display": "flex", "flex-direction": "column"})


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="Type", component_property="value"),
               Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date'),

)


def make_graphs(Type,start_date, end_date):

    # HISTOGRAM
 colors = ['orange', '#dd1e35', 'green', '#e55467']
 if len(Type) > 0:
    dff = df.loc[start_date:end_date]
    dff2=df1.loc[start_date:end_date]
    df_hist = dff[dff["order_source"].isin(Type)]
    fig_hist = px.histogram(dff, x='order_status')
    df_x= px.pie(dff, values='sales_price', names='order_source')
    order = df_hist['order_id'].count()
    revenue = df_hist['sales_price'].sum()

    profit = df_hist['sales_price'].sum() - df_hist['sales_cost'].sum()
    conv = df2['number of v'].count() / df2['order id'].count() * 10

    df_y = px.pie(df_hist, names='delivery_status' , hole=.7,title='Delivery Status by Type',color='delivery_status', template='presentation',
   )
    df_z = px.pie(df_hist, names='order_status' , color='order_status',title='Order Status by Type', template='presentation',
    # color_discrete_map={'Failed':'orange',
                                # 'Done':'#dd1e35'
#}
                                )
    # here we need to link between two tables so we can read this product bought at which date
    grouping2 = df1.groupby(['product_id'])[['sales_price']].sum().reset_index()
    x= grouping2.sort_values(by=['sales_price'], ascending=False).head(3)
    fig = px.bar(x, x='sales_price', y='product_id', orientation='h',title='Top 3 Product', template='presentation',)

    grouping = df_hist.groupby(['customer_id'])[['sales_price']].sum().reset_index()
    df_g = grouping.sort_values(by=['sales_price'], ascending=False).head(5)
    fig2 = px.bar(df_g, x="customer_id", y="sales_price", orientation='v',title='Top 5 Client', template='presentation',)
    gr = df_hist.groupby(['order_date'])[['order_id']].count().reset_index()
    fig3= px.line(gr,y='order_id',title="Active Users Per Date",template='presentation')

    grouping3=df_hist.groupby(['region','order_date'])[['sales_price']].sum().reset_index()
    print(grouping3)
    df_map= px.scatter(grouping3, x="sales_price", y="order_date",
	         size="sales_price", color="region",
                 hover_name="region", log_x=False, size_max=60, title="Sales By Area", template='presentation',)


   

    return [
         html.Div([
              html.Div([html.H3( children='Orders',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ), html.P(order  ,
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40
                       }
                   ), ], className="card_container three columns"),
                    html.Div([html.H3( children='Revenu',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}

                    ), html.P(str(revenue) + ' $ ',
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40}
                   ), ], className="card_container three columns"), 
                   html.Div([html.H3( children='Profit',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ), html.P(str(profit) + ' $ '
                      ,
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40}
                   ), ], className="card_container three columns"),
                     html.Div([html.H3( children='Convertion Rate',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ), html.P(str(conv) + ' % '  ,
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40}
                   ), ], className="card_container three columns"),
                ],
                   

          className="row flex-display"),

          
        
         html.Div([
             html.Div([dcc.Graph(figure=df_y)],className="create_container five columns" ),
              html.Div([dcc.Graph(figure=df_z)], className="create_container five columns"),
              html.Div([dcc.Graph(figure=fig2)], className="create_container five columns"),
             
             
            
        ], className="row flex-display"),
         html.Div([
              html.Div([dcc.Graph(figure=fig3)], className="create_container six columns"),
               html.Div([dcc.Graph(figure=fig)], className="create_container six columns"),
              
             
            
        ], className="row flex-display"),
             html.Div([
              html.Div([dcc.Graph(figure=df_map)], className="create_container twelve columns"),
              
              
             
            
        ], className="row flex-display"),
        ]
        #  html.Div([
        # #      html.Div([dcc.Graph(figure=fig_hist)], className="create_container five columns"),
        # #       html.Div([dcc.Graph(figure=df_x)], className="create_container five columns"),
              
             
            
        # #], className="row flex-display"),
        # ]
 elif len(Type) == 0:
        raise dash.exceptions.PreventUpdate


page_2_layout =  html.Div([
    html.Div([
        dbc.Nav(
            [

                dbc.NavLink(
                    "Get Started", active=True, href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),
            ],
            pills=True,

        ),
        # className="me-1",style={'text-decoration':'none'}),
        # dbc.NavLink("Get Started", href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),

        html.Div(
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Home",href="/page-3")),
                    dbc.NavItem(dbc.NavLink("Operational Level", href="/page-1")),
                    dbc.NavItem(dbc.NavLink("Stratgic Level",active=True, href="/page-2")),
                    dbc.NavItem(dbc.NavLink("About", href="page-4")),
                    dbc.NavItem(dbc.NavLink("Help", href="#", id="btn")), Download(id="download")
                ],
                pills=True,

            )
        )],
        className="navbar"),

    html.Br(),
    html.H1("Strategic Dashboard", style={'textAlign': 'center','color': 'white'}),
    

          html.Br(),


   
    html.Div(
        html.Div([
 
                      html.Br(),
       dcc.DatePickerRange(
        id='my-date-picker-range',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2014, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2021, 12, 30),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt(2014, 1, 1),  # the month initially presented when the user opens the calendar
        start_date=dt(2014, 1, 1).date(),
        end_date=dt(2014, 1, 14).date(),
        display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
        month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=2,  # minimum number of days between start and end date

        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  # session, local, or memory. Default is 'local'

        updatemode='singledate' , # singledate or bothdates. Determines when callback is triggered
        
       # style={'background': '#fff', 'cursor': 'pointer', 'padding': '5px 10px', 'border': '1px solid #ccc','width': '100%'}
    ),
    ],), ),




    html.Div(id="output-div2"),
],className="row flex-display", 
    style={"display": "flex", "flex-direction": "column"})


def sales_pie():
    dff = df.groupby('order_source').sum().reset_index()
    fig = px.pie(dff, names='order_source',
                 values='sales_price')
    fig.update_layout(template='presentation', title='Sales By Distribution Channel')
    return fig


@app.callback(Output(component_id="output-div2", component_property="children"),
               Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date'),
)
def make_graphs(start_date, end_date):
    # HISTOGRAM

    dff = df.loc[start_date:end_date]
    dff2 = df1.loc[start_date:end_date]
    # df_hist = dff[dff["order_source"].isin(Type)]
    # fig_hist = px.histogram(dff, x='order_status')

    churnrate_cal = 3 / dff['customer_id'].count()
    churnrate = churnrate_cal.round(2)
    sticky = round(10 / dff['customer_id'].count() ,2)
    viral_co = 10 / dff['customer_id'].count()
    viral = viral_co.round(2)
    customre_cal = 5 / dff['customer_id'].count()
    customre = customre_cal.round(1)
    conv = df2['number of v'].count() / df2['order id'].count() * 10


    grouping2 = dff.groupby(['order_source', 'order_date'])[['sales_price']].sum().reset_index()
    print(grouping2)
    df_z = px.line(grouping2, x='order_date', y='sales_price', color='order_source',
                   title='ROI By Distribution channel ', template='presentation')

    # grouping3=dff.groupby(['order_source','year'])[['num_invint']].count().reset_index()
    # print(grouping3)
    grouping2 = dff.groupby(['order_source', 'order_date'])[['num_invint']].sum().reset_index()
    df_map = px.line(grouping2, x='order_date', y='num_invint', color='order_source',
                     title='Viral Growth Through different channels', template='presentation')

    return [
        html.Div([
            html.Div([
                html.H6(children='Stickiness',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(str(sticky),
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 40}
                       ),

                html.P('Frequent users',
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Churn Rate',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(str(churnrate * 100) + "%",
                       style={
                           'textAlign': 'center',
                           'color': '#dd1e35',
                           'fontSize': 40}
                       ),

                html.P(
                    "customer loyality",
                    style={
                        'textAlign': 'center',
                        'color': '#dd1e35',
                        'fontSize': 15,
                        'margin-top': '-18px'}
                )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Viral Coefficient',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(viral,
                       style={
                           'textAlign': 'center',
                           'color': 'green',
                           'fontSize': 40}
                       ),

                html.P("measure exposure",
                       style={
                           'textAlign': 'center',
                           'color': 'green',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Customer Retention',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(str(customre * 100) + "%",
                       style={
                           'textAlign': 'center',
                           'color': '#e55467',
                           'fontSize': 40}
                       ),

                html.P("Keeping customers",
                       style={
                           'textAlign': 'center',
                           'color': '#e55467',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns")

        ], className="row flex-display"),

        html.Div([
            html.Div([ dbc.Container([
    dbc.Card([
            dbc.Button('Back', id='back-button',color="primary", className="me-1", style={'display': 'none','background_color':'white'}
                        ),
            dbc.Row(
                dcc.Graph(
                        id='graph',
                        figure=sales_pie()
                    ), justify='center'
            )
    ], )
])], className="create_container six columns"),
            html.Div([dcc.Graph(figure=df_z)], className="create_container six columns"),

        ], className="row flex-display"),

        html.Div([
            html.Div([dcc.Graph(figure=df_map)], className="create_container twelve columns"),

        ], className="row flex-display"),
    ]
@app.callback(
    Output('graph', 'figure'),
    Output('back-button', 'style'), #to hide/unhide the back button
    Input('graph', 'clickData'),    #for getting the vendor name from graph
    Input('back-button', 'n_clicks')
)
def drilldown(click_data,n_clicks):

    # using callback context to check which input was fired
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == 'graph':

        # get vendor name from clickData
        if click_data is not None:
            vendor = click_data['points'][0]['label']

            if vendor in df.order_source.unique():
                # creating df for clicked vendor
                vendor_sales_df = df[df['order_source'] == vendor]

                # generating product sales bar graph
                grouping3 = vendor_sales_df.groupby(['region'])[['sales_price']].sum().reset_index()

                fig =  px.bar(grouping3, y="sales_price",x="region",
                           color="region",

                            )
                fig.update_layout(title='<b>{} Regions of sales<b>'.format(vendor),
                                  showlegend=False, template='presentation')
                return fig, {'display':'block'}     #returning the fig and unhiding the back button

            else:
                return sales_pie(), {'display': 'none'}     #hiding the back button

    else:
        return sales_pie(), {'display':'none'}



page_4_layout  = html.Div([
    html.Div([
        dbc.Nav(
            [

                dbc.NavLink(
            "Get Started",active=True, href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),
            ],
            pills=True,

        ),
            #className="me-1",style={'text-decoration':'none'}),
        #dbc.NavLink("Get Started", href="https://www.youtube.com/watch?v=ZK8gEdCA-Wc&t=7s"),


        html.Div(
dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/page-3")),
        dbc.NavItem(dbc.NavLink("Operational Level", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Stratgic Level", href="/page-2")),
        dbc.NavItem(dbc.NavLink("About", active=True, href="page-4")),
        dbc.NavItem(dbc.NavLink("Help",  href="#", id="btn")),Download(id="download")
    ],
    pills=True,


        )
        )],
        className="navbar"),

    html.Div([

        html.H1("About Us", style={'fontWeight': 'bold', 'color': 'white', 'textAlign': 'center'}),

    ]),


    html.Br(),
    html.Div([
html.P("We are a final year students study Information Technology at university of Khartoum ."
"Our graduation project is about the importance of startups growth in the economic of Sudan."
"We developed a BI solution to help startup’s decision makers to take decisions based on data."
,style = {'fontWeight': 'bold', 'color': 'white', 'textAlign': 'center'},className="create_container four columns")


    ]),

])


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-4':
        return page_4_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here



if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
