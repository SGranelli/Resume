import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc



# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H1("Hi! I'm Soledad Granelli", className="text-warning", style={'font-family':'Arial Black'}),
                    html.H4("From Buenos Aires, Argentina", className="text-white", style={'font-family':'Arial', 'font-weight':'lighter'}),
                    html.P("I have no special talent. I am only passionately curious" + " - A. Einstein", className="text-white text-5 font-italic font-weight-lighter mt-1", style={'font-size': '15px', 'font-family':'Arial'}),
                ],className='card text-white bg-dark border-bottom-0', style={'border': '3px solid black'}),
                dbc.CardBody([
                    html.H4("Reach me @", className="mt-0 mb-1 text-warning", style={'font-family':'Arial Black'}),
                    dbc.CardLink("| Mobile |", href="https://api.whatsapp.com/send?phone=541136758004",
                                 className='text-white ml-0', style={'font-family': 'Arial', 'font-size': '17px'}),
                    dbc.CardLink("| LinkedIn |", href="https://www.linkedin.com/in/soledad-granelli-65235437/",
                                 className='text-white ml-3', style={'font-family': 'Arial', 'font-size': '17px'}),
                    dbc.CardLink("| e-mail |", href="soledad.granelli@gmail.com",
                                 className='text-white ml-3', style={'font-family': 'Arial', 'font-size': '17px'}),
                ],className='card text-white bg-dark border-top-0 border-bottom-0 d-inline-block', style={'border': '3px solid black'}),
                dbc.CardBody([
                    html.H4("Who I am", className="card-title mb-1 text-warning", style={'font-family': 'Arial Black'}),
                    html.P("Dynamic & curious, always looking for the next challenge.", className="card-text mb-0", style={'font-size': '17px', 'font-family':'Arial'}),
                    html.P("Not afraid of working under pressure, used to fast paced environments which provide room for growth and career development.", className="card-text mb-0", style={'font-size': '17px', 'font-family':'Arial'}),
                    html.P("Over 10 years experience in Market Research & 5 years in Media Strategy.", className="card-text mb-0", style={'font-size': '17px', 'font-family':'Arial'}),
                ],className='card text-white bg-dark border-top-0', style={'border': '3px solid black'}),
                dbc.CardImg(src="/assets/SG.png", style={'width': '25.5rem', "margin-left": "auto"}, className='mt-0 card-img-overlay'),
            ]),
        ], width=10),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        dcc.Tabs(id='tabs-example', value='tab-1', children=[
                            dcc.Tab(label='Where I come from', value='tab-1', className='text-uppercase'),
                            dcc.Tab(label='How I got here', value='tab-2', className='text-uppercase'),
                            dcc.Tab(label='What I can add to the table', value='tab-3', className='text-uppercase'),
                            dcc.Tab(label='What I can do', value='tab-4', className='text-uppercase'),
                            dcc.Tab(label='A little extra', value='tab-5', className='text-uppercase'),
                        ],
                                 colors={'border':'grey', 'primary':'black','background':'silver'},
                                 style={'font-family': 'Arial', 'font-weight':'bold','font-size': '16px', 'color':'black'}, className='mr-2',
                                 ),
                        html.Div(id='tabs-example-content'),
                    ])
                ], style={'border': '1px solid black'})
            ]),
        ], width=10),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P(
                        "© Made in Python by Soledad Granelli", className="card-text",style={'font-family': 'Arial', 'font-size': '13px', 'text-align':'right'}),
                ]),
            ],className='card text-white bg-dark border-top-0'),
        ], width=10),
    ],className='mb-2'),
], fluid=True)


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return dbc.Card([
                html.H4('My Work Experience', className='mt-4 mb-0 ml-0', style={'font-size': '17px', 'font-family':'Arial'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Wavemaker_Logo.png", style={'width': '6rem', 'height':'6rem'}, className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Wavemaker Argentina',
                                   className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Head of Business Planning & Strategy', className="ml-3 mt-2",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.P(
                        'In charge of delivering long and short term comms strategies for new business and current clients based on understanding business, consumer and competitive dynamics and brand / product requirements. Management of regular and ad hoc analysis (country and market trends, consumer insights, media and competitive dynamics), consulting a variety of sources (syndicated, third party, proprietary tools and desk research methods).',
                        className="ml-3 mb-2 text-break text-body mb-0 border-top-0 border-bottom-0 border-left-0 border-right-0",
                        style={'font-size': '15px', 'font-family': 'Arial'}),
                    dbc.CardFooter('Jun’19 - Current',
                                   className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'220px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Mindshare_Logo.png", style={'width': '6rem', 'height': '6rem'}, className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Mindshare Argentina',
                                   className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Business & Comms Planning Sr. Manager', className="ml-3 mt-2",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.P(
                        'Team management (up to 5 people), focusing on career & talent development. In charge of managing qualitative & quantitative projects (from project setup to presenting findings). Development of ad hoc projects to better understand consumer insights, country and business dynamics, category and media trends. Assist client leads building comms strategies for new and existing clients.',
                        className="ml-3 mb-2 text-break text-body",
                        style={'font-size': '15px', 'font-family': 'Arial'}),
                    dbc.CardFooter('Aug’17 – Jun’19',
                                   className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'205px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Mindshare_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Mindshare Argentina', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Business Planning Coordinator', className="ml-3 mt-3 mb-3",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('Nov’16 Jun’17', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'170px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Mindshare_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Mindshare Argentina', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Business Planning Analyst', className="ml-3 mt-3 mb-3",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('Mar’14 Nov’16', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ])
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'170px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/VPM_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('VPM Via Publica Movil', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Commercial Assistant', className="ml-3 mt-2",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.P(
                        'In charge of keeping the commercial team up to date with industry, campaign and performance reports. Serving as a link with multiple areas (production, design, administration) to guarantee campaign implementation.',
                        className="ml-3 mb-2 text-break text-body mb-0 border-top-0 border-bottom-0 border-left-0 border-right-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    dbc.CardFooter('Jan’12 Mar’14', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'205px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Zenith_Logo.jpg", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Zenith Media Argentina [Former Brand Connection]', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Research Analyst', className="ml-3 mt-2",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.P(
                        'Perform consumer insights, competitive and industry analysis assisted by syndicated and proprietary tools. Focused, but not limited to provide analysis for the FMCG industry.',
                        className="ml-3 mb-2 text-break text-body mb-0 border-top-0 border-bottom-0 border-left-0 border-right-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    dbc.CardFooter('Dec’10 – Jan’12', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'185px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Teletech_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Teletech Argentina', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Business Planning Specialist', className="ml-3 mt-2",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.P(
                        'Analyze and understand short and long term business effects based on historical patterns [call flow, volume, AHT, absenteeism, attrition], leading presentations for all business units to decide next steps.',
                        className="ml-3 mb-2 text-break text-body mb-0 border-top-0 border-bottom-0 border-left-0 border-right-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    dbc.CardFooter('Dec’09 – Dec’10', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'185px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Teletech_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Teletech Argentina', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Real Time Specialist', className="ml-3 mt-3 mb-3",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('Nov’08 – Dec’09', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'170px'}),
            dbc.CardBody([
                dbc.CardImg(src="/assets/Teletech_Logo.png", style={'width': '6rem', 'height': '6rem'},
                            className='mt-4 mr-0 ml-0'),
                dbc.CardBody([
                    dbc.CardHeader('Teletech Argentina', className="mt-1 border-top-0 border-bottom-0 border-left-0 border-right-0",
                                   style={'font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Sales / CC Representative', className="ml-3 mt-3 mb-3",
                            style={'font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('Nov’05 – Aug’08', className="mt-0 border-top-0 border-bottom-0 border-left-0 border-right-0 d-flex",
                                   style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between','height':'190px'}),
        ],className='border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4')
    elif tab == 'tab-2':
        return dbc.Card([
                html.H4('My Education', className='mt-4 mb-0 ml-0', style={'font-size': '17px', 'font-family':'Arial'}),
            dbc.Card([
                dbc.Card([

                ], className='card-body border-top-0 border-bottom-0 border-left-0 border-right-0 mr-5 ml-0'),
                dbc.Card([
                    dbc.CardImg(src="/assets/Fundacion_Logo.png", className='card-img-center',
                                top=True),
                    dbc.CardHeader('Fundación de Altos Estudios en Ciencias Comerciales', className="mt-0",style={'text-align':'center','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Bachelor degree in Advertising and Strategic Communication', className="mb-2 mt-2",style={'text-align':'center','font-size':'18px','font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('From Aug-2008 to Jul-2011', style={'text-align':'center','font-size': '15px', 'font-family': 'Arial'}),
                ], className='card-body mt-4'),
                dbc.Card([
                    dbc.CardImg(src="/assets/CursoRedes_Logo.png", className='card-img-center',
                                top=True),
                    dbc.CardHeader('Centro REDES, Associated to CONICET', className="mt-0",style={'text-align':'center','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Short Course: Programming in Python', className="mb-3 mt-3",style={'text-align':'center','font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('From Apr-2021 to Jun-2021', className="mt-1", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial'}),
                ], className='card-body mt-4'),
                dbc.Card([
                    dbc.CardImg(src="/assets/Tech_Logo.jpg", className='card-img-center',
                                top=True),
                    dbc.CardHeader('Tech Engineering School', className="mt-4 mb-3",style={'text-align':'center','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    html.H4('Masters in Visual Analytics and Big Data', className="mb-2 mt-2",style={'text-align':'center','font-size': '18px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                    dbc.CardFooter('From Jun-2021 to Jun-2022', className="mt-1", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial'}),
                ], className='card-body mt-4'),
                dbc.Card([

                ], className='card-body border-top-0 border-bottom-0 border-left-0 border-right-0 mr-5 ml-0'),
            ], className='card-deck border-top-0 border-bottom-0 border-left-0 border-right-0 mr-5 ml-0', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        ],className='border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4',style={'height':'auto'})
    elif tab == 'tab-3':
        return dbc.Card([
            html.H4('My Skills', className='mt-4 mb-3 ml-0', style={'font-size': '17px', 'font-family': 'Arial'}),
            dbc.Card([
                dbc.CardHeader('Tools', className="mt-0",style={'width':'30rem','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                dbc.CardBody([
                    html.P('* MS Office & Google Drive Suite', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Syndicated Tools: Kantar Suite [for audience and competitive reports], Sysomos, Infegy, Google Ads, Facebook Insights, Comscore, Adcuality, Admetricks.', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Data management Tools: Tableau, Omniscope, Datorama', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Programming: SQL [for MS Excel Macros], Python', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='border-left-0 border-right-0 ml-5 mr-5 mt-3 mb-3', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
            dbc.Card([
                dbc.CardHeader('Experience', className="mt-0",style={'width':'35.5rem','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                dbc.CardBody([
                    html.P('* Research methods: Qualitative [focus groups] & Quantitative [online surveys, experience with Survey Monkey]. Project setup, sample, questionnaire, execution, data processing, analysis & insights.', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Leading and telling stories through presentations', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* External / Internal presentations', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Team management', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='border-left-0 border-right-0 ml-5 mr-5 mt-3 mb-3', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
            dbc.Card([
                dbc.CardHeader('I am', className="mt-0",style={'width':'30rem','font-size': '16px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                dbc.CardBody([
                    html.P('* Proactive / Methodical / Practical', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* A team player', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Strategic thinker', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Data enthusiast', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                    html.P('* Fluent in English [written + oral]', className="mb-0", style={'font-size': '15px', 'font-family': 'Arial'}),
                ]),
            ], className='border-left-0 border-right-0 ml-5 mr-5 mt-3 mb-3', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        ],className='border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4',style={'height':'auto'})
    elif tab == 'tab-4':
        return dbc.Card([
            html.H4('My Portfolio', className='mt-4 mb-3 ml-0', style={'font-size': '17px', 'font-family': 'Arial'}),
            dbc.Card([
                dbc.Card([
                    dbc.CardImg(src="/assets/Newsroom.jpg", style={'width': '50rem'}, className='ml-2',
                                alt="Card image", top=True),
                    html.H4('Newsroom Dashboard', className="mt-2 mb-2", style={'text-align':'center','font-size': '17px', 'font-family': 'Arial'}),
                    html.P(
                        'A Python project to collect news from Google from up to 5 search terms. Collect, visualize and download data to a CSV',
                        className="mt-2 mb-2", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial'}),
                    dbc.Button("Check it @ GitHub ", color="primary",
                               href="https://github.com/SGranelli/Newsroom_project"),
                ], className='card-body', style={'width': '20rem'}),
                dbc.Card([
                    dbc.CardImg(src="/assets/Campaign Performance.jpg", style={'width': '50rem'}, className='ml-2',
                                alt="Card image", top=True),
                    html.H4('Campaign Performance', className="mt-2 mb-2", style={'text-align':'center','font-size': '17px', 'font-family': 'Arial'}),
                    html.P(
                        'A Tableau project to access digital metrics from various platforms, helping users to easily get insights on the ad campaign',
                        className="mt-2 mb-2", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial'}),
                    dbc.Button("Check it @ Tableau ", color="primary",
                               href="https://public.tableau.com/app/profile/soledad.granelli/viz/Campaignanalysis_16229294927900/CampaignPerformance"),

                ], className='card-body mr-5', style={'width': '20rem'}),
            ], className='card-deck border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4 mr-4', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        ],className='border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4',style={'height':'auto'})

    elif tab == 'tab-5':
        return dbc.Card([
            html.H4('I also enjoy', className='mt-4 mb-3 ml-0', style={'font-size': '17px', 'font-family': 'Arial'}),
            dbc.Card([
                dbc.Card([
                    dbc.CardImg(src="/assets/HealtyFood.png",top=True),
                    html.P('Food, Healthy eating & Cooking', className="mb-0 mt-3", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ], className='card-body mr-5 border-top-0 border-bottom-0 border-left-0 border-right-0', style={'width': '5rem'}),
                dbc.Card([
                    dbc.CardImg(src="/assets/Fitness.jpg", top=True),
                    html.P('Sports & Fitness', className="mb-0 mt-3", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ], className='card-body mr-5 border-top-0 border-bottom-0 border-left-0 border-right-0', style={'width': '5rem'}),
                dbc.Card([
                    dbc.CardImg(src="/assets/Literature.png", top=True),
                    html.P('Literature', className="mb-0 mt-3", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ], className='card-body mr-5 border-top-0 border-bottom-0 border-left-0 border-right-0', style={'width': '5em'}),
                dbc.Card([
                    dbc.CardImg(src="/assets/Cinema.png", top=True),
                    html.P('Cinema', className="mb-0 mt-3", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ], className='card-body mr-5 border-top-0 border-bottom-0 border-left-0 border-right-0', style={'width': '5rem'}),
                dbc.Card([
                    dbc.CardImg(src="/assets/Music.png", top=True),
                    html.P('Music [I’m a drummer]', className="mb-0 mt-3", style={'text-align':'center','font-size': '15px', 'font-family': 'Arial', 'font-weight': 'bold'}),
                ], className='card-body mr-5 border-top-0 border-bottom-0 border-left-0 border-right-0', style={'width': '5rem'}),
            ], className='card-deck border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4 mr-4', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        ],className='border-top-0 border-bottom-0 border-left-0 border-right-0 ml-4',style={'height':'auto'})


if __name__=='__main__':
    app.run_server(debug=True)

