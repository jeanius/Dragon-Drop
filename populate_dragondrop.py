import os
import dragondrop.get_domain_from_url

def populate():

	#Users
	James = User.objects.create_user('James',None, 'Jamespassword')
	James.save()
	Gosel = User.objects.create_user('Gosel',None, 'Goselpassword')
	Gosel.save()
	Jean = User.objects.create_user('Jean',None, 'Jeanpassword')
	Jean.save()
	Wen = User.objects.create_user('Wen',None, 'Wenpassword')
	Wen.save()
	Martyna = User.objects.create_user('Martyna',None, 'Martynapassword')
	Martyna.save()
	Leif = User.objects.create_user('Leif',None, 'Leifpassword')
	James.save()

	#Folders
	f_Misc_Trees_and_Graphs_Wen = add_folder(foldername='Misc Trees and Graphs',fusername_fk=Wen)
	f_Bar_Chart_Gosel = add_folder(foldername='Bar Chart',fusername_fk=Gosel)
	f_Online_Editors_Jean = add_folder(foldername='Online Editors',fusername_fk=Jean)
	f_Misc_Charts_Jean = add_folder(foldername='Misc Charts',fusername_fk=Jean)
	f_Online_Editors_Martyna = add_folder(foldername='Online Editors',fusername_fk=Martyna)
	f_Sunburst_and_Partition_layout_Wen = add_folder(foldername='Sunburst and Partition layout',fusername_fk=Wen)
	f_Evaluation_Gosel = add_folder(foldername='Evaluation',fusername_fk=Gosel)
	f_Useful_snippets_Jean = add_folder(foldername='Useful snippets',fusername_fk=Jean)
	f_Miscellaneous_visualizations_Gosel = add_folder(foldername='Miscellaneous visualizations',fusername_fk=Gosel)
	f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel = add_folder(foldername='Parallel Coordinates Parallel sets and Sankey',fusername_fk=Gosel)
	f_Tree_Wen = add_folder(foldername='Tree',fusername_fk=Wen)
	f_Jason_Davies_James = add_folder(foldername='Jason Davies',fusername_fk=James)
	f_Products_Martyna = add_folder(foldername='Products',fusername_fk=Martyna)
	f_Maps_Jean = add_folder(foldername='Maps',fusername_fk=Jean)
	f_Chord_Layout_Jean = add_folder(foldername='Chord Layout',fusername_fk=Jean)
	f_Histogram_Gosel = add_folder(foldername='Histogram',fusername_fk=Gosel)
	f_Scatterplot_and_Bubble_chart_Gosel = add_folder(foldername='Scatterplot and Bubble chart',fusername_fk=Gosel)
	f_Maps_Gosel = add_folder(foldername='Maps',fusername_fk=Gosel)
	f_Store_Apps_Martyna = add_folder(foldername='Store Apps',fusername_fk=Martyna)
	f_Force_Layout_Wen = add_folder(foldername='Force Layout',fusername_fk=Wen)
	f_Libraries_Martyna = add_folder(foldername='Libraries',fusername_fk=Martyna)
	f_Parallel_Coordinates_Parallel_sets_and_Sankey_Wen = add_folder(foldername='Parallel Coordinates Parallel sets and Sankey',fusername_fk=Wen)
	f_Institute_for_Health_Metrics_and_Evaluation_Gosel = add_folder(foldername='Institute for Health Metrics and Evaluation',fusername_fk=Gosel)
	f_Jim_Vallandingham_James = add_folder(foldername='Jim Vallandingham',fusername_fk=James)
	f_Line_and_Area_Chart_Gosel = add_folder(foldername='Line and Area Chart',fusername_fk=Gosel)
	f_Jerome_Cukier_Martyna = add_folder(foldername='Jerome Cukier',fusername_fk=Martyna)
	f_Chord_Layout_Wen = add_folder(foldername='Chord Layout',fusername_fk=Wen)
	f_Pie_Chart_Gosel = add_folder(foldername='Pie Chart',fusername_fk=Gosel)
	f_Jason_Davies_Martyna = add_folder(foldername='Jason Davies',fusername_fk=Martyna)
	f_Interoperability_Jean = add_folder(foldername='Interoperability',fusername_fk=Jean)
	f_Miscellaneous_visualizations_Jean = add_folder(foldername='Miscellaneous visualizations',fusername_fk=Jean)

	#Bookmarks
	bmID_112,bmID_b_112 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/1046712')
	bmID_112.btitle='Static'
	bmID_112.bdescr='Static'
	bmID_112.save()
	bfID_112 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_112,bfrank=0.848437046882)
	bfID_112.save()
	bmID_206,bmID_b_206 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/sankey')
	bmID_206.btitle='Sankey diagrams from Excel'
	bmID_206.bdescr='Sankey diagrams from Excel'
	bmID_206.save()
	bfID_206 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_206,bfrank=0.162461123631)
	bfID_206.save()
	bmID_174,bmID_b_174 = Bookmark.objects.get_or_create(url='http://gist.github.com/plandem/5683951')
	bmID_174.btitle='Correct zoom for layout'
	bmID_174.bdescr='Correct zoom for layout'
	bmID_174.save()
	bfID_174 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_174,bfrank=0.935376185141)
	bfID_174.save()
	bmID_204,bmID_b_204 = Bookmark.objects.get_or_create(url='http://blog.ouseful.info/2012/05/11/viewing-openlearn-mindmaps-using-d3-js/')
	bmID_204.btitle='Viewing OpenLearn Mindmaps Using d3 js'
	bmID_204.bdescr='Viewing OpenLearn Mindmaps Using d3 js'
	bmID_204.save()
	bfID_204 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_204,bfrank=0.660048533969)
	bfID_204.save()
	bmID_140,bmID_b_140 = Bookmark.objects.get_or_create(url='http://ggruiz.me/explosions/')
	bmID_140.btitle='Explosions'
	bmID_140.bdescr='Explosions'
	bmID_140.save()
	bfID_140 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_140,bfrank=0.569949638143)
	bfID_140.save()
	bmID_62,bmID_b_62 = Bookmark.objects.get_or_create(url='http://xliberation.com/parse/colortable/parsed3.html')
	bmID_62.btitle='Sunburst  Color schemer with parse com integration'
	bmID_62.bdescr='Sunburst  Color schemer with parse com integration'
	bmID_62.save()
	bfID_62 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_62,bfrank=0.10082376533)
	bfID_62.save()
	bmID_56,bmID_b_56 = Bookmark.objects.get_or_create(url='http://www.theage.com.au/national/parsets')
	bmID_56.btitle='Parallel Sets with reorderable heading'
	bmID_56.bdescr='Parallel Sets with reorderable heading'
	bmID_56.save()
	bfID_56 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_56,bfrank=0.296207949075)
	bfID_56.save()
	bmID_155,bmID_b_155 = Bookmark.objects.get_or_create(url='https://github.com/boorad/d3-tsline')
	bmID_155.btitle='Time Series'
	bmID_155.bdescr='Time Series'
	bmID_155.save()
	bfID_155 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_155,bfrank=0.366457444521)
	bfID_155.save()
	bmID_55,bmID_b_55 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/parallel-sets/')
	bmID_55.btitle='Parallel Sets'
	bmID_55.bdescr='Parallel Sets'
	bmID_55.save()
	bfID_55 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_55,bfrank=0.875667674141)
	bfID_55.save()
	bmID_313,bmID_b_313 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/earthquakes/#3.00/20.00/805.00')
	bmID_313.btitle='Latest Earthquakes'
	bmID_313.bdescr='Latest Earthquakes'
	bmID_313.save()
	bfID_313 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_313,bfrank=0.459581856678)
	bfID_313.save()
	bmID_188,bmID_b_188 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4053096')
	bmID_188.btitle='Constraint relaxation 1'
	bmID_188.bdescr='Constraint relaxation 1'
	bmID_188.save()
	bfID_188 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_188,bfrank=0.465029424095)
	bfID_188.save()
	bmID_243,bmID_b_243 = Bookmark.objects.get_or_create(url='https://www.droptask.com')
	bmID_243.btitle='DropTask  Visual task management application using D3 for visuals'
	bmID_243.bdescr='DropTask  Visual task management application using D3 for visuals'
	bmID_243.save()
	bfID_243 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_243,bfrank=0.0232506116331)
	bfID_243.save()
	bmID_184,bmID_b_184 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1691430')
	bmID_184.btitle='Automatic floating labels using d3 force layout'
	bmID_184.bdescr='Automatic floating labels using d3 force layout'
	bmID_184.save()
	bfID_184 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_184,bfrank=0.29640921894)
	bfID_184.save()
	bmID_27,bmID_b_27 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3048166')
	bmID_27.btitle='Fixed width Histogram of Durations  log normal distribution'
	bmID_27.bdescr='Fixed width Histogram of Durations  log normal distribution'
	bmID_27.save()
	bfID_27 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gosel,bfbookmark=bmID_27,bfrank=0.455447858895)
	bfID_27.save()
	bmID_126,bmID_b_126 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2280295')
	bmID_126.btitle='Pictograms'
	bmID_126.bdescr='Pictograms'
	bmID_126.save()
	bfID_126 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_126,bfrank=0.0778219037473)
	bfID_126.save()
	bmID_33,bmID_b_33 = Bookmark.objects.get_or_create(url='http://mpf.vis.ywng.cloudbees.net/')
	bmID_33.btitle='Comprehensive Line Graph'
	bmID_33.bdescr='Comprehensive Line Graph'
	bmID_33.save()
	bfID_33 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_33,bfrank=0.242746353021)
	bfID_33.save()
	bmID_157,bmID_b_157 = Bookmark.objects.get_or_create(url='http://www.larsko.org/v/euc/')
	bmID_157.btitle='Radar chart'
	bmID_157.bdescr='Radar chart'
	bmID_157.save()
	bfID_157 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_157,bfrank=0.0235028689734)
	bfID_157.save()
	bmID_317,bmID_b_317 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-trig/')
	bmID_317.btitle='Animated Trigonometry'
	bmID_317.bdescr='Animated Trigonometry'
	bmID_317.save()
	bfID_317 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_317,bfrank=0.829367132774)
	bfID_317.save()
	bmID_114,bmID_b_114 = Bookmark.objects.get_or_create(url='http://fleetinbeing.net/d3e/chord.html')
	bmID_114.btitle='Chord Layout Transitions'
	bmID_114.bdescr='Chord Layout Transitions'
	bmID_114.save()
	bfID_114 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_114,bfrank=0.272832375003)
	bfID_114.save()
	bmID_311,bmID_b_311 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/gaussian-primes/')
	bmID_311.btitle='Gaussian Primes'
	bmID_311.bdescr='Gaussian Primes'
	bmID_311.save()
	bfID_311 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_311,bfrank=0.195575945676)
	bfID_311.save()
	bmID_52,bmID_b_52 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3921009')
	bmID_52.btitle='Sankey diagram with cycles'
	bmID_52.bdescr='Sankey diagram with cycles'
	bmID_52.save()
	bfID_52 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_52,bfrank=0.354774955981)
	bfID_52.save()
	bmID_316,bmID_b_316 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-bezier/')
	bmID_316.btitle='Animated B zier Curves'
	bmID_316.bdescr='Animated B zier Curves'
	bmID_316.save()
	bfID_316 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_316,bfrank=0.447378610062)
	bfID_316.save()
	bmID_100,bmID_b_100 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4092944')
	bmID_100.btitle='Circular tree comparing the src directory for three versions of d3'
	bmID_100.bdescr='Circular tree comparing the src directory for three versions of d3'
	bmID_100.save()
	bfID_100 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_100,bfrank=0.995506226519)
	bfID_100.save()
	bmID_283,bmID_b_283 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/factorisation-diagrams/')
	bmID_283.btitle='Factorisation Diagrams'
	bmID_283.bdescr='Factorisation Diagrams'
	bmID_283.save()
	bfID_283 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_283,bfrank=0.39339319978)
	bfID_283.save()
	bmID_324,bmID_b_324 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/poincare-disc/')
	bmID_324.btitle='Poincar  Disc'
	bmID_324.bdescr='Poincar  Disc'
	bmID_324.save()
	bfID_324 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_324,bfrank=0.0637684538727)
	bfID_324.save()
	bmID_168,bmID_b_168 = Bookmark.objects.get_or_create(url='http://blog.lightjs.org/2012/10/welcome-to-webplatform-animation-d3js/')
	bmID_168.btitle='Webplatform dancing logo'
	bmID_168.bdescr='Webplatform dancing logo'
	bmID_168.save()
	bfID_168 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_168,bfrank=0.134402103991)
	bfID_168.save()
	bmID_337,bmID_b_337 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/church_by_state.html')
	bmID_337.btitle='Composition of Church Membership by State  1890'
	bmID_337.bdescr='Composition of Church Membership by State  1890'
	bmID_337.save()
	bfID_337 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_337,bfrank=0.239148025053)
	bfID_337.save()
	bmID_277,bmID_b_277 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/segregate.html')
	bmID_277.btitle='Schelling s segregation model'
	bmID_277.bdescr='Schelling s segregation model'
	bmID_277.save()
	bfID_277 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_277,bfrank=0.615262101075)
	bfID_277.save()
	bmID_191,bmID_b_191 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3173233')
	bmID_191.btitle='Loading Adobe Photoshop ASE color palette'
	bmID_191.bdescr='Loading Adobe Photoshop ASE color palette'
	bmID_191.save()
	bfID_191 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_191,bfrank=0.931362642771)
	bfID_191.save()
	bmID_16,bmID_b_16 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/882152')
	bmID_16.btitle='Grouped Bar Chart'
	bmID_16.bdescr='Grouped Bar Chart'
	bmID_16.save()
	bfID_16 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_16,bfrank=0.0825705841163)
	bfID_16.save()
	bmID_113,bmID_b_113 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/1308257')
	bmID_113.btitle='Static'
	bmID_113.bdescr='Static'
	bmID_113.save()
	bfID_113 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_113,bfrank=0.583735352635)
	bfID_113.save()
	bmID_141,bmID_b_141 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1086421')
	bmID_141.btitle='Linear Gradients'
	bmID_141.bdescr='Linear Gradients'
	bmID_141.save()
	bfID_141 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_141,bfrank=0.00168002608249)
	bfID_141.save()
	bmID_137,bmID_b_137 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1117287')
	bmID_137.btitle='Segmented Lines and Slope Coloring'
	bmID_137.bdescr='Segmented Lines and Slope Coloring'
	bmID_137.save()
	bfID_137 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_137,bfrank=0.391001122484)
	bfID_137.save()
	bmID_25,bmID_b_25 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1933560')
	bmID_25.btitle='Histogram Chart'
	bmID_25.bdescr='Histogram Chart'
	bmID_25.save()
	bfID_25 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gosel,bfbookmark=bmID_25,bfrank=0.524164650322)
	bfID_25.save()
	bmID_54,bmID_b_54 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3290263')
	bmID_54.btitle='Parallel coordinates with fisheye distortion'
	bmID_54.bdescr='Parallel coordinates with fisheye distortion'
	bmID_54.save()
	bfID_54 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_54,bfrank=0.446816147511)
	bfID_54.save()
	bmID_61,bmID_b_61 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1005873')
	bmID_61.btitle='Partition Layout  Zoomable Icicle '
	bmID_61.bdescr='Partition Layout  Zoomable Icicle '
	bmID_61.save()
	bfID_61 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_61,bfrank=0.154261910965)
	bfID_61.save()
	bmID_336,bmID_b_336 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/racial_divide.html')
	bmID_336.btitle='Visualizing The Racial Divide'
	bmID_336.bdescr='Visualizing The Racial Divide'
	bmID_336.save()
	bfID_336 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_336,bfrank=0.0586429709119)
	bfID_336.save()
	bmID_2,bmID_b_2 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_2.btitle='US Health Map'
	bmID_2.bdescr='US Health Map'
	bmID_2.save()
	bfID_2 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_2,bfrank=0.995062233461)
	bfID_2.save()
	bmID_335,bmID_b_335 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/movie')
	bmID_335.btitle='We re In The Money  How Much Do The Movies We Love Make '
	bmID_335.bdescr='We re In The Money  How Much Do The Movies We Love Make '
	bmID_335.save()
	bfID_335 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_335,bfrank=0.509393929501)
	bfID_335.save()
	bmID_248,bmID_b_248 = Bookmark.objects.get_or_create(url='http://plot.io/')
	bmID_248.btitle='Plot io  swallowed by Platfora '
	bmID_248.bdescr='Plot io  swallowed by Platfora '
	bmID_248.save()
	bfID_248 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_248,bfrank=0.0542722555396)
	bfID_248.save()
	bmID_158,bmID_b_158 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1629464')
	bmID_158.btitle='Drag rectangle'
	bmID_158.bdescr='Drag rectangle'
	bmID_158.save()
	bfID_158 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_158,bfrank=0.723656302834)
	bfID_158.save()
	bmID_20,bmID_b_20 = Bookmark.objects.get_or_create(url='http://theoldbeggar.com/aid/')
	bmID_20.btitle='Sortable bars  Foreign aid  corruption and internet use'
	bmID_20.bdescr='Sortable bars  Foreign aid  corruption and internet use'
	bmID_20.save()
	bfID_20 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_20,bfrank=0.829674298006)
	bfID_20.save()
	bmID_270,bmID_b_270 = Bookmark.objects.get_or_create(url='http://iop.io/iopctrl')
	bmID_270.btitle='iopctrl js  User interface controls and gauges'
	bmID_270.bdescr='iopctrl js  User interface controls and gauges'
	bmID_270.save()
	bfID_270 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_270,bfrank=0.0391723909953)
	bfID_270.save()
	bmID_274,bmID_b_274 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/ca.html')
	bmID_274.btitle='Cellular automata'
	bmID_274.bdescr='Cellular automata'
	bmID_274.save()
	bfID_274 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_274,bfrank=0.23871652146)
	bfID_274.save()
	bmID_19,bmID_b_19 = Bookmark.objects.get_or_create(url='https://github.com/mlarocca/Dynamic-Charts')
	bmID_19.btitle='Dynamic Bar Charts'
	bmID_19.bdescr='Dynamic Bar Charts'
	bmID_19.save()
	bfID_19 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_19,bfrank=0.941924211923)
	bfID_19.save()
	bmID_110,bmID_b_110 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4062006')
	bmID_110.btitle='Fade on Hover'
	bmID_110.bdescr='Fade on Hover'
	bmID_110.save()
	bfID_110 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_110,bfrank=0.923003866199)
	bfID_110.save()
	bmID_299,bmID_b_299 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/sunflower-phyllotaxis/')
	bmID_299.btitle='Sunflower Phyllotaxis'
	bmID_299.bdescr='Sunflower Phyllotaxis'
	bmID_299.save()
	bfID_299 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_299,bfrank=0.363223293813)
	bfID_299.save()
	bmID_256,bmID_b_256 = Bookmark.objects.get_or_create(url='https://www.moh.io/')
	bmID_256.btitle='Mohiomap  A Visual Memory for Evernote'
	bmID_256.bdescr='Mohiomap  A Visual Memory for Evernote'
	bmID_256.save()
	bfID_256 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_256,bfrank=0.724833249264)
	bfID_256.save()
	bmID_109,bmID_b_109 = Bookmark.objects.get_or_create(url='http://livecoding.io/3419309')
	bmID_109.btitle='Fade on Hover'
	bmID_109.bdescr='Fade on Hover'
	bmID_109.save()
	bfID_109 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_109,bfrank=0.654808416868)
	bfID_109.save()
	bmID_250,bmID_b_250 = Bookmark.objects.get_or_create(url='http://trisul.org/')
	bmID_250.btitle='Trisul Network Analytic'
	bmID_250.bdescr='Trisul Network Analytic'
	bmID_250.save()
	bfID_250 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_250,bfrank=0.165446446599)
	bfID_250.save()
	bmID_92,bmID_b_92 = Bookmark.objects.get_or_create(url='http://maxdemarzi.com/2012/03/08/connections-in-time/')
	bmID_92.btitle='Connections in time'
	bmID_92.bdescr='Connections in time'
	bmID_92.save()
	bfID_92 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_92,bfrank=0.825147578149)
	bfID_92.save()
	bmID_207,bmID_b_207 = Bookmark.objects.get_or_create(url='https://github.com/davidcox/plotsk')
	bmID_207.btitle='Plotsk  A python coffeescript d3 js based library for plotting data in a web browser'
	bmID_207.bdescr='Plotsk  A python coffeescript d3 js based library for plotting data in a web browser'
	bmID_207.save()
	bfID_207 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_207,bfrank=0.873706840311)
	bfID_207.save()
	bmID_21,bmID_b_21 = Bookmark.objects.get_or_create(url='https://github.com/gencay/stackedGroupedChart')
	bmID_21.btitle='Grouped and Stacked Bar Chart'
	bmID_21.bdescr='Grouped and Stacked Bar Chart'
	bmID_21.save()
	bfID_21 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_21,bfrank=0.250218600883)
	bfID_21.save()
	bmID_262,bmID_b_262 = Bookmark.objects.get_or_create(url='http://square.github.com/cubism/')
	bmID_262.btitle='Cubism js  Time Series Visualization'
	bmID_262.bdescr='Cubism js  Time Series Visualization'
	bmID_262.save()
	bfID_262 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_262,bfrank=0.527961820743)
	bfID_262.save()
	bmID_281,bmID_b_281 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/simplify/')
	bmID_281.btitle='Topology Preserving Geometry Simplification'
	bmID_281.bdescr='Topology Preserving Geometry Simplification'
	bmID_281.save()
	bfID_281 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_281,bfrank=0.496162921593)
	bfID_281.save()
	bmID_258,bmID_b_258 = Bookmark.objects.get_or_create(url='http://apps.microsoft.com/windows/en-us/app/presentation-next/57c55802-1bdd-48c9-bf8b-e9e3c24cf051')
	bmID_258.btitle='Presentation Next  A Windows 8 HTML5 SVG Presentation Builder'
	bmID_258.bdescr='Presentation Next  A Windows 8 HTML5 SVG Presentation Builder'
	bmID_258.save()
	bfID_258 = BookmarkToFolder.objects.create(bffolder=f_Store_Apps_Martyna,bfbookmark=bmID_258,bfrank=0.050071466688)
	bfID_258.save()
	bmID_173,bmID_b_173 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/nbremer/raw/6506614/')
	bmID_173.btitle='Radar Chart or Spider Chart'
	bmID_173.bdescr='Radar Chart or Spider Chart'
	bmID_173.save()
	bfID_173 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_173,bfrank=0.174492120432)
	bfID_173.save()
	bmID_9,bmID_b_9 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-uncertainty-visualization')
	bmID_9.btitle='GBD Uncertainty Visualization'
	bmID_9.bdescr='GBD Uncertainty Visualization'
	bmID_9.save()
	bfID_9 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_9,bfrank=0.196108882915)
	bfID_9.save()
	bmID_75,bmID_b_75 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1129492')
	bmID_75.btitle='Bounded Force Layout'
	bmID_75.bdescr='Bounded Force Layout'
	bmID_75.save()
	bfID_75 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_75,bfrank=0.103807202763)
	bfID_75.save()
	bmID_115,bmID_b_115 = Bookmark.objects.get_or_create(url='http://www.rjbaxley.com/p/publications.html')
	bmID_115.btitle='Co Authors Chords'
	bmID_115.bdescr='Co Authors Chords'
	bmID_115.save()
	bfID_115 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_115,bfrank=0.0542732977131)
	bfID_115.save()
	bmID_49,bmID_b_49 = Bookmark.objects.get_or_create(url='http://benjiec.github.io/scatter-matrix/demo/demo.html')
	bmID_49.btitle='Explore Matrix Data with Scatterplots'
	bmID_49.bdescr='Explore Matrix Data with Scatterplots'
	bmID_49.save()
	bfID_49 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_49,bfrank=0.253579300153)
	bfID_49.save()
	bmID_53,bmID_b_53 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1341281')
	bmID_53.btitle='Parallel Coordinates'
	bmID_53.bdescr='Parallel Coordinates'
	bmID_53.save()
	bfID_53 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_53,bfrank=0.667186690165)
	bfID_53.save()
	bmID_3,bmID_b_3 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_3.btitle='US Health Map'
	bmID_3.bdescr='US Health Map'
	bmID_3.save()
	bfID_3 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_3,bfrank=0.263142867439)
	bfID_3.save()
	bmID_170,bmID_b_170 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/d/2361485/')
	bmID_170.btitle='Life expectancy  small multiples'
	bmID_170.bdescr='Life expectancy  small multiples'
	bmID_170.save()
	bfID_170 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_170,bfrank=0.976472821477)
	bfID_170.save()
	bmID_217,bmID_b_217 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2294676')
	bmID_217.btitle='SVG to Canvas'
	bmID_217.bdescr='SVG to Canvas'
	bmID_217.save()
	bfID_217 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_217,bfrank=0.0597461587049)
	bfID_217.save()
	bmID_264,bmID_b_264 = Bookmark.objects.get_or_create(url='https://github.com/shutterstock/rickshaw')
	bmID_264.btitle='Rickshaw  JavaScript toolkit for creating interactive real time graphs'
	bmID_264.bdescr='Rickshaw  JavaScript toolkit for creating interactive real time graphs'
	bmID_264.save()
	bfID_264 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_264,bfrank=0.687550127053)
	bfID_264.save()
	bmID_239,bmID_b_239 = Bookmark.objects.get_or_create(url='http://phrogz.net/JS/d3-playground/#BlankDefault')
	bmID_239.btitle='D3 js playground'
	bmID_239.bdescr='D3 js playground'
	bmID_239.save()
	bfID_239 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_239,bfrank=0.974871200333)
	bfID_239.save()
	bmID_273,bmID_b_273 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/markov.html')
	bmID_273.btitle='Markov processes'
	bmID_273.bdescr='Markov processes'
	bmID_273.save()
	bfID_273 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_273,bfrank=0.427061848026)
	bfID_273.save()
	bmID_271,bmID_b_271 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/nuitblanche.html')
	bmID_271.btitle='La Nuit Blanche'
	bmID_271.bdescr='La Nuit Blanche'
	bmID_271.save()
	bfID_271 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_271,bfrank=0.951810009233)
	bfID_271.save()
	bmID_22,bmID_b_22 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/rsloan/7123450')
	bmID_22.btitle='Waterfall Chart'
	bmID_22.bdescr='Waterfall Chart'
	bmID_22.save()
	bfID_22 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_22,bfrank=0.475643193895)
	bfID_22.save()
	bmID_227,bmID_b_227 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/partition')
	bmID_227.btitle='Zoomable Partition Charts directly from Excel'
	bmID_227.bdescr='Zoomable Partition Charts directly from Excel'
	bmID_227.save()
	bfID_227 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_227,bfrank=0.409790497682)
	bfID_227.save()
	bmID_68,bmID_b_68 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/950642')
	bmID_68.btitle='Images and Labels'
	bmID_68.bdescr='Images and Labels'
	bmID_68.save()
	bfID_68 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_68,bfrank=0.693210769576)
	bfID_68.save()
	bmID_259,bmID_b_259 = Bookmark.objects.get_or_create(url='http://nickqizhu.github.com/dc.js/')
	bmID_259.btitle='Dc js'
	bmID_259.bdescr='Dc js'
	bmID_259.save()
	bfID_259 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_259,bfrank=0.342970733455)
	bfID_259.save()
	bmID_65,bmID_b_65 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021841')
	bmID_65.btitle='Custom Forces'
	bmID_65.bdescr='Custom Forces'
	bmID_65.save()
	bfID_65 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_65,bfrank=0.156590421581)
	bfID_65.save()
	bmID_224,bmID_b_224 = Bookmark.objects.get_or_create(url='http://maxdemarzi.com/2012/02/13/visualizing-a-network-with-cypher/')
	bmID_224.btitle='Visualizing a network with Cypher and d3 js'
	bmID_224.bdescr='Visualizing a network with Cypher and d3 js'
	bmID_224.save()
	bfID_224 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_224,bfrank=0.817959397084)
	bfID_224.save()
	bmID_310,bmID_b_310 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hilbert-curve/')
	bmID_310.btitle='Hilbert Curve'
	bmID_310.bdescr='Hilbert Curve'
	bmID_310.save()
	bfID_310 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_310,bfrank=0.941180083093)
	bfID_310.save()
	bmID_43,bmID_b_43 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1346395')
	bmID_43.btitle='Pie Chart Updating  Part 1 '
	bmID_43.bdescr='Pie Chart Updating  Part 1 '
	bmID_43.save()
	bfID_43 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gosel,bfbookmark=bmID_43,bfrank=0.85237398182)
	bfID_43.save()
	bmID_192,bmID_b_192 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/shawnbot/BJLe6/')
	bmID_192.btitle='Render sever side using Phantomjs'
	bmID_192.bdescr='Render sever side using Phantomjs'
	bmID_192.save()
	bfID_192 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_192,bfrank=0.375548136265)
	bfID_192.save()
	bmID_95,bmID_b_95 = Bookmark.objects.get_or_create(url='http://thepowerrank.com/visual/NCAA_Tournament_Predictions')
	bmID_95.btitle='Circular tree  Will your team win the NCAA Tournament '
	bmID_95.bdescr='Circular tree  Will your team win the NCAA Tournament '
	bmID_95.save()
	bfID_95 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_95,bfrank=0.809066029017)
	bfID_95.save()
	bmID_41,bmID_b_41 = Bookmark.objects.get_or_create(url='https://github.com/gajus/pie-chart')
	bmID_41.btitle='Reusable Pie Charts'
	bmID_41.bdescr='Reusable Pie Charts'
	bmID_41.save()
	bfID_41 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gosel,bfbookmark=bmID_41,bfrank=0.777609555233)
	bfID_41.save()
	bmID_213,bmID_b_213 = Bookmark.objects.get_or_create(url='https://github.com/asutherland/d3-threeD')
	bmID_213.btitle='Very limited  in progress attempt to hook d3 js up to three js'
	bmID_213.bdescr='Very limited  in progress attempt to hook d3 js up to three js'
	bmID_213.save()
	bfID_213 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_213,bfrank=0.594794270784)
	bfID_213.save()
	bmID_97,bmID_b_97 = Bookmark.objects.get_or_create(url='http://bit.ly/PvWgUH')
	bmID_97.btitle='SCION simulation environment'
	bmID_97.bdescr='SCION simulation environment'
	bmID_97.save()
	bfID_97 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_97,bfrank=0.785462862527)
	bfID_97.save()
	bmID_276,bmID_b_276 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/polya.html')
	bmID_276.btitle='The Polya process'
	bmID_276.bdescr='The Polya process'
	bmID_276.save()
	bfID_276 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_276,bfrank=0.79986658507)
	bfID_276.save()
	bmID_12,bmID_b_12 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/life-expectancy-county-and-sex-us-country-comparison-global-1989-1999-2009')
	bmID_12.btitle='Life expectancy by county and sex  US  with country comparison'
	bmID_12.bdescr='Life expectancy by county and sex  US  with country comparison'
	bmID_12.save()
	bfID_12 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_12,bfrank=0.101167462209)
	bfID_12.save()
	bmID_327,bmID_b_327 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/tuebingen/')
	bmID_327.btitle='T bingen'
	bmID_327.bdescr='T bingen'
	bmID_327.save()
	bfID_327 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_327,bfrank=0.396618501845)
	bfID_327.save()
	bmID_69,bmID_b_69 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2883411')
	bmID_69.btitle='Drag and Drop Support to set nodes to fixed position when dropped'
	bmID_69.bdescr='Drag and Drop Support to set nodes to fixed position when dropped'
	bmID_69.save()
	bfID_69 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_69,bfrank=0.615638335433)
	bfID_69.save()
	bmID_185,bmID_b_185 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/3689677')
	bmID_185.btitle='Long Scroll'
	bmID_185.bdescr='Long Scroll'
	bmID_185.save()
	bfID_185 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_185,bfrank=0.117320806735)
	bfID_185.save()
	bmID_149,bmID_b_149 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1243323')
	bmID_149.btitle='Merge Sort'
	bmID_149.bdescr='Merge Sort'
	bmID_149.save()
	bfID_149 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_149,bfrank=0.206187353838)
	bfID_149.save()
	bmID_46,bmID_b_46 = Bookmark.objects.get_or_create(url='http://slodge.com/teach/')
	bmID_46.btitle='Animated bubble charts for school data analysis'
	bmID_46.bdescr='Animated bubble charts for school data analysis'
	bmID_46.save()
	bfID_46 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_46,bfrank=0.994182655829)
	bfID_46.save()
	bmID_251,bmID_b_251 = Bookmark.objects.get_or_create(url='http://exploreanalytics.com/')
	bmID_251.btitle='Explore Analytics  cloud based data analytics and visualization'
	bmID_251.bdescr='Explore Analytics  cloud based data analytics and visualization'
	bmID_251.save()
	bfID_251 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_251,bfrank=0.766731748563)
	bfID_251.save()
	bmID_181,bmID_b_181 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1343714')
	bmID_181.btitle='Bay Area earthquake responses by zip code  loading external file through Yahoo Pipes'
	bmID_181.bdescr='Bay Area earthquake responses by zip code  loading external file through Yahoo Pipes'
	bmID_181.save()
	bfID_181 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_181,bfrank=0.5063383486)
	bfID_181.save()
	bmID_238,bmID_b_238 = Bookmark.objects.get_or_create(url='http://enjalot.com/tributary/2165875/sinwaves.js')
	bmID_238.btitle='Tributary'
	bmID_238.bdescr='Tributary'
	bmID_238.save()
	bfID_238 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_238,bfrank=0.710096699698)
	bfID_238.save()
	bmID_59,bmID_b_59 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/910126')
	bmID_59.btitle='Sunburst Layout with Labels'
	bmID_59.bdescr='Sunburst Layout with Labels'
	bmID_59.save()
	bfID_59 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_59,bfrank=0.178416726884)
	bfID_59.save()
	bmID_285,bmID_b_285 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/set-partitions/')
	bmID_285.btitle='Set Partitions'
	bmID_285.bdescr='Set Partitions'
	bmID_285.save()
	bfID_285 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_285,bfrank=0.441355310451)
	bfID_285.save()
	bmID_186,bmID_b_186 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3310323')
	bmID_186.btitle='Custom Line Interpolation'
	bmID_186.bdescr='Custom Line Interpolation'
	bmID_186.save()
	bfID_186 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_186,bfrank=0.615546098834)
	bfID_186.save()
	bmID_314,bmID_b_314 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/tree-of-life/')
	bmID_314.btitle='Phylogenetic Tree of Life'
	bmID_314.bdescr='Phylogenetic Tree of Life'
	bmID_314.save()
	bfID_314 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_314,bfrank=0.259794974186)
	bfID_314.save()
	bmID_88,bmID_b_88 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/999346')
	bmID_88.btitle='Animated'
	bmID_88.bdescr='Animated'
	bmID_88.save()
	bfID_88 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_88,bfrank=0.569766269635)
	bfID_88.save()
	bmID_237,bmID_b_237 = Bookmark.objects.get_or_create(url='http://livecoding.gabrielflor.it')
	bmID_237.btitle='Live coding based on Bret Victor s Inventing on Principle talk'
	bmID_237.bdescr='Live coding based on Bret Victor s Inventing on Principle talk'
	bmID_237.save()
	bfID_237 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_237,bfrank=0.43569646427)
	bfID_237.save()
	bmID_50,bmID_b_50 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/llb4ll/8709363')
	bmID_50.btitle='k Nearest Neighbor Search with Quadtree'
	bmID_50.bdescr='k Nearest Neighbor Search with Quadtree'
	bmID_50.save()
	bfID_50 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_50,bfrank=0.47613574202)
	bfID_50.save()
	bmID_29,bmID_b_29 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1166403')
	bmID_29.btitle='Axis Component'
	bmID_29.bdescr='Axis Component'
	bmID_29.save()
	bfID_29 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_29,bfrank=0.476951283835)
	bfID_29.save()
	bmID_205,bmID_b_205 = Bookmark.objects.get_or_create(url='https://bitbucket.org/davidagraf/dartsplaytree/src')
	bmID_205.btitle='Splay Tree animation with dart  d3  and local storage'
	bmID_205.bdescr='Splay Tree animation with dart  d3  and local storage'
	bmID_205.save()
	bfID_205 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_205,bfrank=0.400572851678)
	bfID_205.save()
	bmID_216,bmID_b_216 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1846692')
	bmID_216.btitle='Automatically sizing text'
	bmID_216.bdescr='Automatically sizing text'
	bmID_216.save()
	bfID_216 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_216,bfrank=0.752493492573)
	bfID_216.save()
	bmID_98,bmID_b_98 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/972398')
	bmID_98.btitle='Treemap Layout in SVG'
	bmID_98.bdescr='Treemap Layout in SVG'
	bmID_98.save()
	bfID_98 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_98,bfrank=0.165729600075)
	bfID_98.save()
	bmID_72,bmID_b_72 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1080941')
	bmID_72.btitle='From XML'
	bmID_72.bdescr='From XML'
	bmID_72.save()
	bfID_72 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_72,bfrank=0.189759302204)
	bfID_72.save()
	bmID_136,bmID_b_136 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1016220')
	bmID_136.btitle='Line Tension'
	bmID_136.bdescr='Line Tension'
	bmID_136.save()
	bfID_136 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_136,bfrank=0.73596964032)
	bfID_136.save()
	bmID_295,bmID_b_295 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/9patch/')
	bmID_295.btitle='9 Patch Quilt Generator'
	bmID_295.bdescr='9 Patch Quilt Generator'
	bmID_295.save()
	bfID_295 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_295,bfrank=0.219822014257)
	bfID_295.save()
	bmID_71,bmID_b_71 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062288')
	bmID_71.btitle='Collapsible Hierarchy'
	bmID_71.bdescr='Collapsible Hierarchy'
	bmID_71.save()
	bfID_71 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_71,bfrank=0.10990301467)
	bfID_71.save()
	bmID_234,bmID_b_234 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/gassites/d3-concept-browser')
	bmID_234.btitle='Force directed site concept browser'
	bmID_234.bdescr='Force directed site concept browser'
	bmID_234.save()
	bfID_234 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_234,bfrank=0.908598806062)
	bfID_234.save()
	bmID_175,bmID_b_175 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1071269')
	bmID_175.btitle='Date Ticks'
	bmID_175.bdescr='Date Ticks'
	bmID_175.save()
	bfID_175 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_175,bfrank=0.175571280339)
	bfID_175.save()
	bmID_96,bmID_b_96 = Bookmark.objects.get_or_create(url='http://blockses.appspot.com/2503502')
	bmID_96.btitle='Bracket Layout'
	bmID_96.bdescr='Bracket Layout'
	bmID_96.save()
	bfID_96 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_96,bfrank=0.425654575351)
	bfID_96.save()
	bmID_242,bmID_b_242 = Bookmark.objects.get_or_create(url='http://www.ubiq.co')
	bmID_242.btitle='Ubiq Analytics  MySQL Analytics  amp  Reporting made easy'
	bmID_242.bdescr='Ubiq Analytics  MySQL Analytics  amp  Reporting made easy'
	bmID_242.save()
	bfID_242 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_242,bfrank=0.541753923103)
	bfID_242.save()
	bmID_101,bmID_b_101 = Bookmark.objects.get_or_create(url='http://jimkang.com/quadtreevis/')
	bmID_101.btitle='Interactive visualization that shows changes in the internal node tree of a quadtree as points are added'
	bmID_101.bdescr='Interactive visualization that shows changes in the internal node tree of a quadtree as points are added'
	bmID_101.save()
	bfID_101 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_101,bfrank=0.261970323255)
	bfID_101.save()
	bmID_120,bmID_b_120 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1067636')
	bmID_120.btitle='Venn Diagram using Clipping'
	bmID_120.bdescr='Venn Diagram using Clipping'
	bmID_120.save()
	bfID_120 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_120,bfrank=0.13033844333)
	bfID_120.save()
	bmID_171,bmID_b_171 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4589092')
	bmID_171.btitle='Semi manual force layout of cablegate reference graphs'
	bmID_171.bdescr='Semi manual force layout of cablegate reference graphs'
	bmID_171.save()
	bfID_171 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_171,bfrank=0.721557301156)
	bfID_171.save()
	bmID_40,bmID_b_40 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/nswamy14/083a1e3181c81428f817')
	bmID_40.btitle='Overlapped distribution Area chart'
	bmID_40.bdescr='Overlapped distribution Area chart'
	bmID_40.save()
	bfID_40 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_40,bfrank=0.986790762398)
	bfID_40.save()
	bmID_269,bmID_b_269 = Bookmark.objects.get_or_create(url='http://sepans.com/sp/postes/lepracursor/')
	bmID_269.btitle='Lepracursor'
	bmID_269.bdescr='Lepracursor'
	bmID_269.save()
	bfID_269 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_269,bfrank=0.221610247832)
	bfID_269.save()
	bmID_244,bmID_b_244 = Bookmark.objects.get_or_create(url='https://bitdeli.com/')
	bmID_244.btitle='Bitdeli  Custom analytics with Python and GitHub'
	bmID_244.bdescr='Bitdeli  Custom analytics with Python and GitHub'
	bmID_244.save()
	bfID_244 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_244,bfrank=0.64453349133)
	bfID_244.save()
	bmID_121,bmID_b_121 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1067616')
	bmID_121.btitle='Venn Diagram using Opacity'
	bmID_121.bdescr='Venn Diagram using Opacity'
	bmID_121.save()
	bfID_121 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_121,bfrank=0.50464682555)
	bfID_121.save()
	bmID_23,bmID_b_23 = Bookmark.objects.get_or_create(url='https://github.com/liufly/Dual-scale-D3-Bar-Chart')
	bmID_23.btitle='Dual scale Bar Chart'
	bmID_23.bdescr='Dual scale Bar Chart'
	bmID_23.save()
	bfID_23 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_23,bfrank=0.113172593482)
	bfID_23.save()
	bmID_37,bmID_b_37 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1314483')
	bmID_37.btitle='Stacked layout with time axis'
	bmID_37.bdescr='Stacked layout with time axis'
	bmID_37.save()
	bfID_37 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_37,bfrank=0.449213453034)
	bfID_37.save()
	bmID_179,bmID_b_179 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1846692')
	bmID_179.btitle='Automatically sizing text'
	bmID_179.bdescr='Automatically sizing text'
	bmID_179.save()
	bfID_179 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_179,bfrank=0.228885816655)
	bfID_179.save()
	bmID_266,bmID_b_266 = Bookmark.objects.get_or_create(url='http://tenxer.github.com/xcharts/')
	bmID_266.btitle='xCharts  a D3 based library for building custom charts and graphs'
	bmID_266.bdescr='xCharts  a D3 based library for building custom charts and graphs'
	bmID_266.save()
	bfID_266 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_266,bfrank=0.54537945655)
	bfID_266.save()
	bmID_15,bmID_b_15 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1283663')
	bmID_15.btitle='Hierarchical Bar Chart'
	bmID_15.bdescr='Hierarchical Bar Chart'
	bmID_15.save()
	bfID_15 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_15,bfrank=0.357966097397)
	bfID_15.save()
	bmID_26,bmID_b_26 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3048450')
	bmID_26.btitle='Fixed width Histogram  Irwin Hall distribution'
	bmID_26.bdescr='Fixed width Histogram  Irwin Hall distribution'
	bmID_26.save()
	bfID_26 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gosel,bfbookmark=bmID_26,bfrank=0.503854784355)
	bfID_26.save()
	bmID_86,bmID_b_86 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/murray_3/5q62y/8/')
	bmID_86.btitle='Collpase expand nodes of a tree'
	bmID_86.bdescr='Collpase expand nodes of a tree'
	bmID_86.save()
	bfID_86 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_86,bfrank=0.0935596740212)
	bfID_86.save()
	bmID_272,bmID_b_272 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/percolate.html')
	bmID_272.btitle='Percolation model'
	bmID_272.bdescr='Percolation model'
	bmID_272.save()
	bfID_272 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_272,bfrank=0.0715543359905)
	bfID_272.save()
	bmID_294,bmID_b_294 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bml/')
	bmID_294.btitle='Biham Middleton Levine Traffic Model'
	bmID_294.bdescr='Biham Middleton Levine Traffic Model'
	bmID_294.save()
	bfID_294 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_294,bfrank=0.99850131174)
	bfID_294.save()
	bmID_268,bmID_b_268 = Bookmark.objects.get_or_create(url='https://github.com/ignacioola/insights')
	bmID_268.btitle='Insights  Interactive Force Graph Component'
	bmID_268.bdescr='Insights  Interactive Force Graph Component'
	bmID_268.save()
	bfID_268 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_268,bfrank=0.313219327112)
	bfID_268.save()
	bmID_177,bmID_b_177 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1367999')
	bmID_177.btitle='PJAX'
	bmID_177.bdescr='PJAX'
	bmID_177.save()
	bfID_177 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_177,bfrank=0.839774760393)
	bfID_177.save()
	bmID_142,bmID_b_142 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1073373')
	bmID_142.btitle='Force Directed States of America'
	bmID_142.bdescr='Force Directed States of America'
	bmID_142.save()
	bfID_142 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_142,bfrank=0.788283313961)
	bfID_142.save()
	bmID_132,bmID_b_132 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021103')
	bmID_132.btitle='Superformula Explorer'
	bmID_132.bdescr='Superformula Explorer'
	bmID_132.save()
	bfID_132 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_132,bfrank=0.828733815113)
	bfID_132.save()
	bmID_80,bmID_b_80 = Bookmark.objects.get_or_create(url='http://pmsangal.tumblr.com/post/65499782255/visualizing-web-performance-1')
	bmID_80.btitle='Web performance'
	bmID_80.bdescr='Web performance'
	bmID_80.save()
	bfID_80 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_80,bfrank=0.842663525959)
	bfID_80.save()
	bmID_315,bmID_b_315 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/voroboids/')
	bmID_315.btitle='Voronoi Boids  Voroboids'
	bmID_315.bdescr='Voronoi Boids  Voroboids'
	bmID_315.save()
	bfID_315 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_315,bfrank=0.708694512781)
	bfID_315.save()
	bmID_4,bmID_b_4 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/gbd-compare/')
	bmID_4.btitle='GBD Compare'
	bmID_4.bdescr='GBD Compare'
	bmID_4.save()
	bfID_4 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gosel,bfbookmark=bmID_4,bfrank=0.279691387513)
	bfID_4.save()
	bmID_190,bmID_b_190 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3605124')
	bmID_190.btitle='Axis Examples'
	bmID_190.bdescr='Axis Examples'
	bmID_190.save()
	bfID_190 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_190,bfrank=0.531907729167)
	bfID_190.save()
	bmID_235,bmID_b_235 = Bookmark.objects.get_or_create(url='http://www.d3-generator.com/')
	bmID_235.btitle='Bar chart code generator and online editor'
	bmID_235.bdescr='Bar chart code generator and online editor'
	bmID_235.save()
	bfID_235 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Jean,bfbookmark=bmID_235,bfrank=0.811213183506)
	bfID_235.save()
	bmID_24,bmID_b_24 = Bookmark.objects.get_or_create(url='https://github.com/gajus/interdependent-interactive-histograms')
	bmID_24.btitle='Reusable Interdependent Interactive Histograms'
	bmID_24.bdescr='Reusable Interdependent Interactive Histograms'
	bmID_24.save()
	bfID_24 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gosel,bfbookmark=bmID_24,bfrank=0.238105446947)
	bfID_24.save()
	bmID_326,bmID_b_326 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/random-polygon-ellipse/')
	bmID_326.btitle='From Random Polygon to Ellipse'
	bmID_326.bdescr='From Random Polygon to Ellipse'
	bmID_326.save()
	bfID_326 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_326,bfrank=0.0160095855658)
	bfID_326.save()
	bmID_178,bmID_b_178 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1226718')
	bmID_178.btitle='Table Sorting'
	bmID_178.bdescr='Table Sorting'
	bmID_178.save()
	bfID_178 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_178,bfrank=0.177638075218)
	bfID_178.save()
	bmID_14,bmID_b_14 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/development-assistance-health-channel-assistance-global-1990-2011-interacti')
	bmID_14.btitle='Development assistance for health by channel of assistance'
	bmID_14.bdescr='Development assistance for health by channel of assistance'
	bmID_14.save()
	bfID_14 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_14,bfrank=0.551525573413)
	bfID_14.save()
	bmID_47,bmID_b_47 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/indiemaps/gzPDU/')
	bmID_47.btitle='Scatterplot and Heatmap'
	bmID_47.bdescr='Scatterplot and Heatmap'
	bmID_47.save()
	bfID_47 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_47,bfrank=0.967190793374)
	bfID_47.save()
	bmID_90,bmID_b_90 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1249394')
	bmID_90.btitle='Collapsible  with Labels'
	bmID_90.bdescr='Collapsible  with Labels'
	bmID_90.save()
	bfID_90 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_90,bfrank=0.356570929556)
	bfID_90.save()
	bmID_127,bmID_b_127 = Bookmark.objects.get_or_create(url='http://dyninc.github.com/d3-smokechart/')
	bmID_127.btitle='Smoke charts'
	bmID_127.bdescr='Smoke charts'
	bmID_127.save()
	bfID_127 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_127,bfrank=0.81871207817)
	bfID_127.save()
	bmID_212,bmID_b_212 = Bookmark.objects.get_or_create(url='http://www.benh.co.uk/datasift/visualising-a-datasift-feed-with-node-and-d3/')
	bmID_212.btitle='Visualising a real time DataSift feed with Node and D3 js'
	bmID_212.bdescr='Visualising a real time DataSift feed with Node and D3 js'
	bmID_212.save()
	bfID_212 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_212,bfrank=0.750485813194)
	bfID_212.save()
	bmID_222,bmID_b_222 = Bookmark.objects.get_or_create(url='http://css.dzone.com/articles/render-geographic-information')
	bmID_222.btitle='Render Geographic Information in 3D With Three js and D3 js'
	bmID_222.bdescr='Render Geographic Information in 3D With Three js and D3 js'
	bmID_222.save()
	bfID_222 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_222,bfrank=0.737146787044)
	bfID_222.save()
	bmID_125,bmID_b_125 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1962173')
	bmID_125.btitle='Swimlane Chart'
	bmID_125.bdescr='Swimlane Chart'
	bmID_125.save()
	bfID_125 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_125,bfrank=0.997313834741)
	bfID_125.save()
	bmID_138,bmID_b_138 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/849853')
	bmID_138.btitle='Raindrops'
	bmID_138.bdescr='Raindrops'
	bmID_138.save()
	bfID_138 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_138,bfrank=0.422916136939)
	bfID_138.save()
	bmID_252,bmID_b_252 = Bookmark.objects.get_or_create(url='http://meshu.io/')
	bmID_252.btitle='Meshu turns your places into beautiful objects '
	bmID_252.bdescr='Meshu turns your places into beautiful objects '
	bmID_252.save()
	bfID_252 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_252,bfrank=0.269510550967)
	bfID_252.save()
	bmID_107,bmID_b_107 = Bookmark.objects.get_or_create(url='http://exposedata.com/tutorial/chord/latest.html')
	bmID_107.btitle='Updating data'
	bmID_107.bdescr='Updating data'
	bmID_107.save()
	bfID_107 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_107,bfrank=0.75675537967)
	bfID_107.save()
	bmID_103,bmID_b_103 = Bookmark.objects.get_or_create(url='http://www.nu.nl/files/datajournalistiek/ek/ek2012.htm#.UKJ5yuOe8ww')
	bmID_103.btitle='Selecties EK 2012'
	bmID_103.bdescr='Selecties EK 2012'
	bmID_103.save()
	bfID_103 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_103,bfrank=0.441426937567)
	bfID_103.save()
	bmID_7,bmID_b_7 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-heatmap')
	bmID_7.btitle='GBD Heatmap'
	bmID_7.bdescr='GBD Heatmap'
	bmID_7.save()
	bfID_7 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_7,bfrank=0.972416083172)
	bfID_7.save()
	bmID_161,bmID_b_161 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1552725')
	bmID_161.btitle='alpha shapes aka concave hulls'
	bmID_161.bdescr='alpha shapes aka concave hulls'
	bmID_161.save()
	bfID_161 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_161,bfrank=0.0765962707899)
	bfID_161.save()
	bmID_219,bmID_b_219 = Bookmark.objects.get_or_create(url='http://webmonarch.github.com/d34raphael/usage.html')
	bmID_219.btitle='d34raphael'
	bmID_219.bdescr='d34raphael'
	bmID_219.save()
	bfID_219 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_219,bfrank=0.443636849059)
	bfID_219.save()
	bmID_260,bmID_b_260 = Bookmark.objects.get_or_create(url='http://nvd3.org/')
	bmID_260.btitle='NVD3'
	bmID_260.bdescr='NVD3'
	bmID_260.save()
	bfID_260 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_260,bfrank=0.202449200788)
	bfID_260.save()
	bmID_249,bmID_b_249 = Bookmark.objects.get_or_create(url='http://chart.io/')
	bmID_249.btitle='Chart io  The Easiest Business Dashboard You ll Ever Use'
	bmID_249.bdescr='Chart io  The Easiest Business Dashboard You ll Ever Use'
	bmID_249.save()
	bfID_249 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_249,bfrank=0.59399419845)
	bfID_249.save()
	bmID_17,bmID_b_17 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1134768')
	bmID_17.btitle='Stacked Bar Chart'
	bmID_17.bdescr='Stacked Bar Chart'
	bmID_17.save()
	bfID_17 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_17,bfrank=0.717961836835)
	bfID_17.save()
	bmID_265,bmID_b_265 = Bookmark.objects.get_or_create(url='https://github.com/vogievetsky/DVL')
	bmID_265.btitle='Dynamic Visualization LEGO'
	bmID_265.bdescr='Dynamic Visualization LEGO'
	bmID_265.save()
	bfID_265 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_265,bfrank=0.766950626131)
	bfID_265.save()
	bmID_6,bmID_b_6 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/cod/')
	bmID_6.btitle='COD Visualization'
	bmID_6.bdescr='COD Visualization'
	bmID_6.save()
	bfID_6 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gosel,bfbookmark=bmID_6,bfrank=0.432099503483)
	bfID_6.save()
	bmID_200,bmID_b_200 = Bookmark.objects.get_or_create(url='http://www.drewconway.com/zia/?p=2765')
	bmID_200.btitle='Visualizing NetworkX graphs in the browser using D3'
	bmID_200.bdescr='Visualizing NetworkX graphs in the browser using D3'
	bmID_200.save()
	bfID_200 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_200,bfrank=0.477949508332)
	bfID_200.save()
	bmID_82,bmID_b_82 = Bookmark.objects.get_or_create(url='http://disqus.com/gravity')
	bmID_82.btitle='Gravity by Disqus'
	bmID_82.bdescr='Gravity by Disqus'
	bmID_82.save()
	bfID_82 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_82,bfrank=0.708912113579)
	bfID_82.save()
	bmID_284,bmID_b_284 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bubbles/')
	bmID_284.btitle='Bubbles'
	bmID_284.bdescr='Bubbles'
	bmID_284.save()
	bfID_284 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_284,bfrank=0.537496091835)
	bfID_284.save()
	bmID_93,bmID_b_93 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/voronoi-diagram-with-force-directed-nodes-and-delaunay-links/')
	bmID_93.btitle='Voronoi Diagram with Force Directed Nodes and Delaunay Links'
	bmID_93.bdescr='Voronoi Diagram with Force Directed Nodes and Delaunay Links'
	bmID_93.save()
	bfID_93 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_93,bfrank=0.948419463649)
	bfID_93.save()
	bmID_108,bmID_b_108 = Bookmark.objects.get_or_create(url='http://fleetinbeing.net/d3e/chord.html')
	bmID_108.btitle='Updating data'
	bmID_108.bdescr='Updating data'
	bmID_108.save()
	bfID_108 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_108,bfrank=0.564262938709)
	bfID_108.save()
	bmID_45,bmID_b_45 = Bookmark.objects.get_or_create(url='http://www.ericbullington.com/articles/2012/01/31/kmeans-visualization')
	bmID_45.btitle='Scatterplot for K Means clustering visualization'
	bmID_45.bdescr='Scatterplot for K Means clustering visualization'
	bmID_45.save()
	bfID_45 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_45,bfrank=0.945099949035)
	bfID_45.save()
	bmID_312,bmID_b_312 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/wave/')
	bmID_312.btitle='Wave'
	bmID_312.bdescr='Wave'
	bmID_312.save()
	bfID_312 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_312,bfrank=0.297840669448)
	bfID_312.save()
	bmID_130,bmID_b_130 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3543186')
	bmID_130.btitle='Spiral for John Hunter'
	bmID_130.bdescr='Spiral for John Hunter'
	bmID_130.save()
	bfID_130 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_130,bfrank=0.57332688233)
	bfID_130.save()
	bmID_246,bmID_b_246 = Bookmark.objects.get_or_create(url='http://square.github.com/tesseract/')
	bmID_246.btitle='Fast Multidimensional Filtering for Coordinated Views'
	bmID_246.bdescr='Fast Multidimensional Filtering for Coordinated Views'
	bmID_246.save()
	bfID_246 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_246,bfrank=0.267362051257)
	bfID_246.save()
	bmID_131,bmID_b_131 = Bookmark.objects.get_or_create(url='http://nbremer.blogspot.com/2013/07/self-organizing-maps-adding-boundaries.html')
	bmID_131.btitle='Hexagonal Heatmaps for e g  Self Organizing Maps'
	bmID_131.bdescr='Hexagonal Heatmaps for e g  Self Organizing Maps'
	bmID_131.save()
	bfID_131 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_131,bfrank=0.320248103874)
	bfID_131.save()
	bmID_261,bmID_b_261 = Bookmark.objects.get_or_create(url='http://dimplejs.org/')
	bmID_261.btitle='Dimple'
	bmID_261.bdescr='Dimple'
	bmID_261.save()
	bfID_261 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_261,bfrank=0.839609718886)
	bfID_261.save()
	bmID_297,bmID_b_297 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/planarity/')
	bmID_297.btitle='Planarity'
	bmID_297.bdescr='Planarity'
	bmID_297.save()
	bfID_297 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_297,bfrank=0.787769085322)
	bfID_297.save()
	bmID_73,bmID_b_73 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2846454')
	bmID_73.btitle='From Matrix Market format'
	bmID_73.bdescr='From Matrix Market format'
	bmID_73.save()
	bfID_73 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_73,bfrank=0.192199407919)
	bfID_73.save()
	bmID_255,bmID_b_255 = Bookmark.objects.get_or_create(url='http://www.infocaptor.com')
	bmID_255.btitle='InfoCaptor Dashboards with D3 and canvas'
	bmID_255.bdescr='InfoCaptor Dashboards with D3 and canvas'
	bmID_255.save()
	bfID_255 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_255,bfrank=0.635087036455)
	bfID_255.save()
	bmID_143,bmID_b_143 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1123639')
	bmID_143.btitle='Rounded Rectangles'
	bmID_143.bdescr='Rounded Rectangles'
	bmID_143.save()
	bfID_143 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_143,bfrank=0.474951556716)
	bfID_143.save()
	bmID_193,bmID_b_193 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4236639')
	bmID_193.btitle='Reusable text rotation'
	bmID_193.bdescr='Reusable text rotation'
	bmID_193.save()
	bfID_193 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_193,bfrank=0.896807813179)
	bfID_193.save()
	bmID_330,bmID_b_330 = Bookmark.objects.get_or_create(url='http://vallandingham.me/bubble_cloud/')
	bmID_330.btitle='Word Frequency Bubble Clouds'
	bmID_330.bdescr='Word Frequency Bubble Clouds'
	bmID_330.save()
	bfID_330 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_330,bfrank=0.580709615121)
	bfID_330.save()
	bmID_106,bmID_b_106 = Bookmark.objects.get_or_create(url='http://bost.ocks.org/mike/uberdata/')
	bmID_106.btitle='Uber Rides by Neighborhood'
	bmID_106.bdescr='Uber Rides by Neighborhood'
	bmID_106.save()
	bfID_106 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_106,bfrank=0.390601865899)
	bfID_106.save()
	bmID_60,bmID_b_60 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/coffee-wheel/')
	bmID_60.btitle='Sunburst  Coffee Flavour Wheel'
	bmID_60.bdescr='Sunburst  Coffee Flavour Wheel'
	bmID_60.save()
	bfID_60 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_60,bfrank=0.238684577851)
	bfID_60.save()
	bmID_194,bmID_b_194 = Bookmark.objects.get_or_create(url='http://ollieglass.com/2012/04/21/bieber-fever-meter-with-html5s-web-socket-d3-js-and-pusher/')
	bmID_194.btitle='Bieber Fever Meter with HTML5 s Web Socket  d3 js and Pusher'
	bmID_194.bdescr='Bieber Fever Meter with HTML5 s Web Socket  d3 js and Pusher'
	bmID_194.save()
	bfID_194 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_194,bfrank=0.993212209943)
	bfID_194.save()
	bmID_35,bmID_b_35 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1483226')
	bmID_35.btitle='Horizon Chart'
	bmID_35.bdescr='Horizon Chart'
	bmID_35.save()
	bfID_35 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_35,bfrank=0.254524724735)
	bfID_35.save()
	bmID_229,bmID_b_229 = Bookmark.objects.get_or_create(url='http://timelyportfolio.blogspot.com/2012/12/d3-shiny-and-r-reporting-performance.html')
	bmID_229.btitle='Web reporting with D3js and R using RStudio Shiny'
	bmID_229.bdescr='Web reporting with D3js and R using RStudio Shiny'
	bmID_229.save()
	bfID_229 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_229,bfrank=0.879483975302)
	bfID_229.save()
	bmID_199,bmID_b_199 = Bookmark.objects.get_or_create(url='http://github.com/jakevdp/mpld3')
	bmID_199.btitle='mpld3  d3 visualizations of matplotlib  python  plots'
	bmID_199.bdescr='mpld3  d3 visualizations of matplotlib  python  plots'
	bmID_199.save()
	bfID_199 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_199,bfrank=0.515158782535)
	bfID_199.save()
	bmID_57,bmID_b_57 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4168921')
	bmID_57.btitle='Pair Contribution and Selection'
	bmID_57.bdescr='Pair Contribution and Selection'
	bmID_57.save()
	bfID_57 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_57,bfrank=0.788308491129)
	bfID_57.save()
	bmID_231,bmID_b_231 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/parse/d3parse')
	bmID_231.btitle='d3 js partition chart serving data from parse com'
	bmID_231.bdescr='d3 js partition chart serving data from parse com'
	bmID_231.save()
	bfID_231 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_231,bfrank=0.0500169652027)
	bfID_231.save()
	bmID_152,bmID_b_152 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1345853')
	bmID_152.btitle='Transform Transitions'
	bmID_152.bdescr='Transform Transitions'
	bmID_152.save()
	bfID_152 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_152,bfrank=0.952269737004)
	bfID_152.save()
	bmID_147,bmID_b_147 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1256572')
	bmID_147.btitle='Show Reel'
	bmID_147.bdescr='Show Reel'
	bmID_147.save()
	bfID_147 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_147,bfrank=0.54320354971)
	bfID_147.save()
	bmID_182,bmID_b_182 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/7WQjr/')
	bmID_182.btitle='Simple HTML data tables'
	bmID_182.bdescr='Simple HTML data tables'
	bmID_182.save()
	bfID_182 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_182,bfrank=0.446340046263)
	bfID_182.save()
	bmID_301,bmID_b_301 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/calkin-wilf-tree/')
	bmID_301.btitle='Calkin Wilf Tree'
	bmID_301.bdescr='Calkin Wilf Tree'
	bmID_301.save()
	bfID_301 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_301,bfrank=0.433011072328)
	bfID_301.save()
	bmID_292,bmID_b_292 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/wordcloud/#http%3A%2F%2Fsearch.twitter.com%2Fsearch.json%3Frpp%3D100%26q%3D%7Bword%7D=cloud')
	bmID_292.btitle='Tag Cloud'
	bmID_292.bdescr='Tag Cloud'
	bmID_292.save()
	bfID_292 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_292,bfrank=0.707094673664)
	bfID_292.save()
	bmID_135,bmID_b_135 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062544')
	bmID_135.btitle='OMG Particles '
	bmID_135.bdescr='OMG Particles '
	bmID_135.save()
	bfID_135 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_135,bfrank=0.96635733296)
	bfID_135.save()
	bmID_94,bmID_b_94 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/building-cubic-hamiltonian-graphs-from-lcf-notation/')
	bmID_94.btitle='Building Cubic Hamiltonian Graphs from LCF Notation'
	bmID_94.bdescr='Building Cubic Hamiltonian Graphs from LCF Notation'
	bmID_94.save()
	bfID_94 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_94,bfrank=0.961281394047)
	bfID_94.save()
	bmID_129,bmID_b_129 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1044242')
	bmID_129.btitle='Hierarchical Edge Bundling'
	bmID_129.bdescr='Hierarchical Edge Bundling'
	bmID_129.save()
	bfID_129 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_129,bfrank=0.117023220759)
	bfID_129.save()
	bmID_18,bmID_b_18 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1327441')
	bmID_18.btitle='Reorderable Stacked Bar Chart'
	bmID_18.bdescr='Reorderable Stacked Bar Chart'
	bmID_18.save()
	bfID_18 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gosel,bfbookmark=bmID_18,bfrank=0.0798209150139)
	bfID_18.save()
	bmID_236,bmID_b_236 = Bookmark.objects.get_or_create(url='http://www.bangongyun.com/chart')
	bmID_236.btitle='D3 bar chart online editor Chinese'
	bmID_236.bdescr='D3 bar chart online editor Chinese'
	bmID_236.save()
	bfID_236 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Jean,bfbookmark=bmID_236,bfrank=0.291300210339)
	bfID_236.save()
	bmID_8,bmID_b_8 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-arrow-diagram')
	bmID_8.btitle='GBD Arrow Diagram'
	bmID_8.bdescr='GBD Arrow Diagram'
	bmID_8.save()
	bfID_8 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_8,bfrank=0.477658631326)
	bfID_8.save()
	bmID_89,bmID_b_89 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1061834')
	bmID_89.btitle='Collapsible'
	bmID_89.bdescr='Collapsible'
	bmID_89.save()
	bfID_89 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_89,bfrank=0.166883591353)
	bfID_89.save()
	bmID_329,bmID_b_329 = Bookmark.objects.get_or_create(url='http://flowingdata.com/2012/08/02/how-to-make-an-interactive-network-visualization/')
	bmID_329.btitle='How to Make an Interactive Network Visualization'
	bmID_329.bdescr='How to Make an Interactive Network Visualization'
	bmID_329.save()
	bfID_329 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_329,bfrank=0.669960281606)
	bfID_329.save()
	bmID_233,bmID_b_233 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/flights')
	bmID_233.btitle='US Airline performance bigdata direct from Google Fusion'
	bmID_233.bdescr='US Airline performance bigdata direct from Google Fusion'
	bmID_233.save()
	bfID_233 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_233,bfrank=0.596937757777)
	bfID_233.save()
	bmID_38,bmID_b_38 = Bookmark.objects.get_or_create(url='http://tympanus.net/codrops/2012/08/29/multiple-area-charts-with-d3-js/')
	bmID_38.btitle='Multiple Area Charts with D3 JS'
	bmID_38.bdescr='Multiple Area Charts with D3 JS'
	bmID_38.save()
	bfID_38 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_38,bfrank=0.314891221483)
	bfID_38.save()
	bmID_180,bmID_b_180 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2295155')
	bmID_180.btitle='Templating ala Mustache  with Chernoff faces example'
	bmID_180.bdescr='Templating ala Mustache  with Chernoff faces example'
	bmID_180.save()
	bfID_180 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_180,bfrank=0.207428261395)
	bfID_180.save()
	bmID_220,bmID_b_220 = Bookmark.objects.get_or_create(url='http://www.dotuscomus.com/pergola/pergola_1.4.0/ExamplesHTML/D3/multiD3.html')
	bmID_220.btitle='D3 graphics in a Pergola SVG UI'
	bmID_220.bdescr='D3 graphics in a Pergola SVG UI'
	bmID_220.save()
	bfID_220 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_220,bfrank=0.2211383608)
	bfID_220.save()
	bmID_300,bmID_b_300 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/girko-circle/')
	bmID_300.btitle='Girko s Circular Law'
	bmID_300.bdescr='Girko s Circular Law'
	bmID_300.save()
	bfID_300 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_300,bfrank=0.82225390003)
	bfID_300.save()
	bmID_167,bmID_b_167 = Bookmark.objects.get_or_create(url='http://exposedata.com/hypercube/rotate/')
	bmID_167.btitle='Rotating hypercube in orthogonal projection and parallel coordinates'
	bmID_167.bdescr='Rotating hypercube in orthogonal projection and parallel coordinates'
	bmID_167.save()
	bfID_167 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_167,bfrank=0.273254802723)
	bfID_167.save()
	bmID_28,bmID_b_28 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1624660')
	bmID_28.btitle='Variable width Histogram'
	bmID_28.bdescr='Variable width Histogram'
	bmID_28.save()
	bfID_28 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gosel,bfbookmark=bmID_28,bfrank=0.766657252139)
	bfID_28.save()
	bmID_245,bmID_b_245 = Bookmark.objects.get_or_create(url='http://square.github.com/cube/')
	bmID_245.btitle='Cube  Time Series Data Collection  amp  Analysis'
	bmID_245.bdescr='Cube  Time Series Data Collection  amp  Analysis'
	bmID_245.save()
	bfID_245 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_245,bfrank=0.334696050675)
	bfID_245.save()
	bmID_44,bmID_b_44 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/4710330/94a7c0aeb6f09d681dbfdd0e5150578e4935c6ae')
	bmID_44.btitle='Hierarchical Pie Chart'
	bmID_44.bdescr='Hierarchical Pie Chart'
	bmID_44.save()
	bfID_44 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gosel,bfbookmark=bmID_44,bfrank=0.363729606465)
	bfID_44.save()
	bmID_241,bmID_b_241 = Bookmark.objects.get_or_create(url='http://cssdeck.com/labs/d3-repulsive')
	bmID_241.btitle='CSSdeck  Repulsion example'
	bmID_241.bdescr='CSSdeck  Repulsion example'
	bmID_241.save()
	bfID_241 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_241,bfrank=0.114420898314)
	bfID_241.save()
	bmID_164,bmID_b_164 = Bookmark.objects.get_or_create(url='http://bollwyvl.github.com/blockd3/')
	bmID_164.btitle='Dataflow programming with D3 and Blockly'
	bmID_164.bdescr='Dataflow programming with D3 and Blockly'
	bmID_164.save()
	bfID_164 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_164,bfrank=0.162185053183)
	bfID_164.save()
	bmID_150,bmID_b_150 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1353700')
	bmID_150.btitle='Epicyclic Gearing'
	bmID_150.bdescr='Epicyclic Gearing'
	bmID_150.save()
	bfID_150 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_150,bfrank=0.670083369081)
	bfID_150.save()
	bmID_210,bmID_b_210 = Bookmark.objects.get_or_create(url='http://blog.echen.me/2012/03/05/instant-interactive-visualization-with-d3-and-ggplot2/')
	bmID_210.btitle='Instant interactive visualization with d3   ggplot2'
	bmID_210.bdescr='Instant interactive visualization with d3   ggplot2'
	bmID_210.save()
	bfID_210 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_210,bfrank=0.111546837548)
	bfID_210.save()
	bmID_308,bmID_b_308 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hamming-quilt/')
	bmID_308.btitle='Hamming Quilt'
	bmID_308.bdescr='Hamming Quilt'
	bmID_308.save()
	bfID_308 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_308,bfrank=0.00616924209561)
	bfID_308.save()
	bmID_197,bmID_b_197 = Bookmark.objects.get_or_create(url='http://blogs.infoecho.net/echo/2012/02/05/ipython-notebook-d3-js-mashup/')
	bmID_197.btitle='IPython Notebook with d3 js'
	bmID_197.bdescr='IPython Notebook with d3 js'
	bmID_197.save()
	bfID_197 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_197,bfrank=0.464702292244)
	bfID_197.save()
	bmID_163,bmID_b_163 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3287802')
	bmID_163.btitle='Simple Dashboard Example'
	bmID_163.bdescr='Simple Dashboard Example'
	bmID_163.save()
	bfID_163 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_163,bfrank=0.550315856896)
	bfID_163.save()
	bmID_119,bmID_b_119 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2206590')
	bmID_119.btitle='Click to Zoom with Albers Projection'
	bmID_119.bdescr='Click to Zoom with Albers Projection'
	bmID_119.save()
	bfID_119 = BookmarkToFolder.objects.create(bffolder=f_Maps_Jean,bfbookmark=bmID_119,bfrank=0.66090093271)
	bfID_119.save()
	bmID_195,bmID_b_195 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4246925')
	bmID_195.btitle='Reverse Geocoding Plug in using an offline canvas'
	bmID_195.bdescr='Reverse Geocoding Plug in using an offline canvas'
	bmID_195.save()
	bfID_195 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_195,bfrank=0.0987530013717)
	bfID_195.save()
	bmID_334,bmID_b_334 = Bookmark.objects.get_or_create(url='http://vallandingham.me/feltronifier/')
	bmID_334.btitle='Feltronifier'
	bmID_334.bdescr='Feltronifier'
	bmID_334.save()
	bfID_334 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_334,bfrank=0.121249826497)
	bfID_334.save()
	bmID_320,bmID_b_320 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/sorting/')
	bmID_320.btitle='Sorting Visualisations'
	bmID_320.bdescr='Sorting Visualisations'
	bmID_320.save()
	bfID_320 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_320,bfrank=0.615720922244)
	bfID_320.save()
	bmID_64,bmID_b_64 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062383')
	bmID_64.btitle='Symbols'
	bmID_64.bdescr='Symbols'
	bmID_64.save()
	bfID_64 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_64,bfrank=0.653341758665)
	bfID_64.save()
	bmID_203,bmID_b_203 = Bookmark.objects.get_or_create(url='http://drsm79.github.com/Backbone-d3/index.html')
	bmID_203.btitle='Backbone D3'
	bmID_203.bdescr='Backbone D3'
	bmID_203.save()
	bfID_203 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_203,bfrank=0.310071630638)
	bfID_203.save()
	bmID_339,bmID_b_339 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/jobs_by_state.html')
	bmID_339.btitle='http   vallandingham me vis jobs_by_state html'
	bmID_339.bdescr='http   vallandingham me vis jobs_by_state html'
	bmID_339.save()
	bfID_339 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_339,bfrank=0.0392377924829)
	bfID_339.save()
	bmID_305,bmID_b_305 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/17x17/')
	bmID_305.btitle='Number of unique rectangle free 4 colourings for an nxm grid'
	bmID_305.bdescr='Number of unique rectangle free 4 colourings for an nxm grid'
	bmID_305.save()
	bfID_305 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_305,bfrank=0.258609529262)
	bfID_305.save()
	bmID_218,bmID_b_218 = Bookmark.objects.get_or_create(url='https://github.com/mhemesath/r2d3/')
	bmID_218.btitle='d3 rendered with RaphaelJS for IE Compatibility'
	bmID_218.bdescr='d3 rendered with RaphaelJS for IE Compatibility'
	bmID_218.save()
	bfID_218 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_218,bfrank=0.967685650031)
	bfID_218.save()
	bmID_13,bmID_b_13 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/development-assistance-health-health-focus-area-global-1990-2009-interactiv')
	bmID_13.btitle='Development assistance for health by health focus area'
	bmID_13.bdescr='Development assistance for health by health focus area'
	bmID_13.save()
	bfID_13 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_13,bfrank=0.649999082763)
	bfID_13.save()
	bmID_286,bmID_b_286 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/primos/')
	bmID_286.btitle='El Patr n de los N meros Primos'
	bmID_286.bdescr='El Patr n de los N meros Primos'
	bmID_286.save()
	bfID_286 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_286,bfrank=0.870054423697)
	bfID_286.save()
	bmID_209,bmID_b_209 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/anyforce')
	bmID_209.btitle='d3 js force diagrams straight from Excel'
	bmID_209.bdescr='d3 js force diagrams straight from Excel'
	bmID_209.save()
	bfID_209 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_209,bfrank=0.980244682779)
	bfID_209.save()
	bmID_78,bmID_b_78 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/chicago-lobbyists-force-directed-graph-visualization/')
	bmID_78.btitle='Chicago Lobbyists'
	bmID_78.bdescr='Chicago Lobbyists'
	bmID_78.save()
	bfID_78 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_78,bfrank=0.404431584535)
	bfID_78.save()
	bmID_223,bmID_b_223 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2759731')
	bmID_223.btitle='D3 heatmap using Backbone js and CoffeeScript'
	bmID_223.bdescr='D3 heatmap using Backbone js and CoffeeScript'
	bmID_223.save()
	bfID_223 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_223,bfrank=0.829472655825)
	bfID_223.save()
	bmID_247,bmID_b_247 = Bookmark.objects.get_or_create(url='http://polychart.com/')
	bmID_247.btitle='Polychart  A browser based platform for exploring data and creating charts'
	bmID_247.bdescr='Polychart  A browser based platform for exploring data and creating charts'
	bmID_247.save()
	bfID_247 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_247,bfrank=0.990615524906)
	bfID_247.save()
	bmID_111,bmID_b_111 = Bookmark.objects.get_or_create(url='http://www.javainc.com/projects/dex/examples/vis/d3/presidents/presidentPartyChord.html')
	bmID_111.btitle='Fade on Hover'
	bmID_111.bdescr='Fade on Hover'
	bmID_111.save()
	bfID_111 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_111,bfrank=0.660429346123)
	bfID_111.save()
	bmID_102,bmID_b_102 = Bookmark.objects.get_or_create(url='http://www.tips-for-excel.com/MCFC/Passes.html')
	bmID_102.btitle='Football passes'
	bmID_102.bdescr='Football passes'
	bmID_102.save()
	bfID_102 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_102,bfrank=0.591726571659)
	bfID_102.save()
	bmID_36,bmID_b_36 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1629644')
	bmID_36.btitle='Line Chart with tooltips'
	bmID_36.bdescr='Line Chart with tooltips'
	bmID_36.save()
	bfID_36 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_36,bfrank=0.468600726502)
	bfID_36.save()
	bmID_332,bmID_b_332 = Bookmark.objects.get_or_create(url='http://stowers.org/stowersreport/maps')
	bmID_332.btitle='Stowers Group Collaboration Network'
	bmID_332.bdescr='Stowers Group Collaboration Network'
	bmID_332.save()
	bfID_332 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_332,bfrank=0.292902282967)
	bfID_332.save()
	bmID_76,bmID_b_76 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1377729')
	bmID_76.btitle='Force Based Label Placement'
	bmID_76.bdescr='Force Based Label Placement'
	bmID_76.save()
	bfID_76 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_76,bfrank=0.274758240625)
	bfID_76.save()
	bmID_117,bmID_b_117 = Bookmark.objects.get_or_create(url='http://redotheweb.com/DependencyWheel/')
	bmID_117.btitle='Visualizing Package Dependencies'
	bmID_117.bdescr='Visualizing Package Dependencies'
	bmID_117.save()
	bfID_117 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_117,bfrank=0.234654615989)
	bfID_117.save()
	bmID_144,bmID_b_144 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1136236')
	bmID_144.btitle='Spermatozoa'
	bmID_144.bdescr='Spermatozoa'
	bmID_144.save()
	bfID_144 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_144,bfrank=0.17849596696)
	bfID_144.save()
	bmID_169,bmID_b_169 = Bookmark.objects.get_or_create(url='http://metro.ezyang.com/')
	bmID_169.btitle='Metro Maps of the News'
	bmID_169.bdescr='Metro Maps of the News'
	bmID_169.save()
	bfID_169 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_169,bfrank=0.90630733256)
	bfID_169.save()
	bmID_304,bmID_b_304 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/coffee-wheel/')
	bmID_304.btitle='Coffee Flavour Wheel'
	bmID_304.bdescr='Coffee Flavour Wheel'
	bmID_304.save()
	bfID_304 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_304,bfrank=0.796059450501)
	bfID_304.save()
	bmID_156,bmID_b_156 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1405439')
	bmID_156.btitle='Voronoi based point picker'
	bmID_156.bdescr='Voronoi based point picker'
	bmID_156.save()
	bfID_156 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_156,bfrank=0.456005652573)
	bfID_156.save()
	bmID_280,bmID_b_280 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/random-points/')
	bmID_280.btitle='Random Points on a Sphere'
	bmID_280.bdescr='Random Points on a Sphere'
	bmID_280.save()
	bfID_280 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_280,bfrank=0.440050065)
	bfID_280.save()
	bmID_253,bmID_b_253 = Bookmark.objects.get_or_create(url='http://www.simple.com/blog/Simple/announcing-reports')
	bmID_253.btitle='Reports for Simple'
	bmID_253.bdescr='Reports for Simple'
	bmID_253.save()
	bfID_253 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_253,bfrank=0.830361302241)
	bfID_253.save()
	bmID_278,bmID_b_278 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/antipodes/')
	bmID_278.btitle='Antipodes'
	bmID_278.bdescr='Antipodes'
	bmID_278.save()
	bfID_278 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_278,bfrank=0.716860704295)
	bfID_278.save()
	bmID_148,bmID_b_148 = Bookmark.objects.get_or_create(url='http://vvvvjs.quasipartikel.at/')
	bmID_148.btitle='VVVV viewer'
	bmID_148.bdescr='VVVV viewer'
	bmID_148.save()
	bfID_148 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_148,bfrank=0.500634046864)
	bfID_148.save()
	bmID_296,bmID_b_296 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/graph-music/')
	bmID_296.btitle='The Music of Graphs'
	bmID_296.bdescr='The Music of Graphs'
	bmID_296.save()
	bfID_296 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_296,bfrank=0.327887622935)
	bfID_296.save()
	bmID_166,bmID_b_166 = Bookmark.objects.get_or_create(url='http://latentflip.github.com/violin/')
	bmID_166.btitle='Violin  Instrumenting JavaScript'
	bmID_166.bdescr='Violin  Instrumenting JavaScript'
	bmID_166.save()
	bfID_166 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_166,bfrank=0.114886937955)
	bfID_166.save()
	bmID_275,bmID_b_275 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/life.html')
	bmID_275.btitle='Game of life'
	bmID_275.bdescr='Game of life'
	bmID_275.save()
	bfID_275 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_275,bfrank=0.81578625273)
	bfID_275.save()
	bmID_307,bmID_b_307 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/collatz-graph/')
	bmID_307.btitle='Collatz Graph  All Numbers Lead to One'
	bmID_307.bdescr='Collatz Graph  All Numbers Lead to One'
	bmID_307.save()
	bfID_307 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_307,bfrank=0.761925794268)
	bfID_307.save()
	bmID_214,bmID_b_214 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/plaliberte/HAXyd/')
	bmID_214.btitle='SVG to Canvas to PNG using Canvg'
	bmID_214.bdescr='SVG to Canvas to PNG using Canvg'
	bmID_214.save()
	bfID_214 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_214,bfrank=0.81340482206)
	bfID_214.save()
	bmID_85,bmID_b_85 = Bookmark.objects.get_or_create(url='http://blog.pixelingene.com/2011/08/progressive-reveal-animations-in-svg-using-a-svgclippath/')
	bmID_85.btitle='Reveal animation on a tree with a clip path'
	bmID_85.bdescr='Reveal animation on a tree with a clip path'
	bmID_85.save()
	bfID_85 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_85,bfrank=0.468296978083)
	bfID_85.save()
	bmID_232,bmID_b_232 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/gassites/d3nodefocus')
	bmID_232.btitle='Force directed node focus generated from Excel'
	bmID_232.bdescr='Force directed node focus generated from Excel'
	bmID_232.save()
	bfID_232 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_232,bfrank=0.0413340123463)
	bfID_232.save()
	bmID_66,bmID_b_66 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021953')
	bmID_66.btitle='Multiple Foci'
	bmID_66.bdescr='Multiple Foci'
	bmID_66.save()
	bfID_66 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_66,bfrank=0.94916626863)
	bfID_66.save()
	bmID_51,bmID_b_51 = Bookmark.objects.get_or_create(url='http://nickrabinowitz.com/projects/d3/alluvial/alluvial-dynamic.html')
	bmID_51.btitle='Animated Sankey Diagram  alluvial '
	bmID_51.bdescr='Animated Sankey Diagram  alluvial '
	bmID_51.save()
	bfID_51 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gosel,bfbookmark=bmID_51,bfrank=0.569695570172)
	bfID_51.save()
	bmID_159,bmID_b_159 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1706523')
	bmID_159.btitle='Elastic collisions'
	bmID_159.bdescr='Elastic collisions'
	bmID_159.save()
	bfID_159 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_159,bfrank=0.103374385894)
	bfID_159.save()
	bmID_0,bmID_b_0 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_0.btitle='US Health Map'
	bmID_0.bdescr='US Health Map'
	bmID_0.save()
	bfID_0 = BookmarkToFolder.objects.create(bffolder=f_Maps_Gosel,bfbookmark=bmID_0,bfrank=0.442626712458)
	bfID_0.save()
	bmID_187,bmID_b_187 = Bookmark.objects.get_or_create(url='http://d3export.cancan.cshl.edu/')
	bmID_187.btitle='Export to SVG PNG PDF server side using Perl'
	bmID_187.bdescr='Export to SVG PNG PDF server side using Perl'
	bmID_187.save()
	bfID_187 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_187,bfrank=0.0315554641573)
	bfID_187.save()
	bmID_118,bmID_b_118 = Bookmark.objects.get_or_create(url='http://nbremer.blogspot.nl/2014/02/switching-behavior-between-phone-brands.html')
	bmID_118.btitle='Switching behavior between phone brands of the Dutch '
	bmID_118.bdescr='Switching behavior between phone brands of the Dutch '
	bmID_118.save()
	bfID_118 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_118,bfrank=0.0704037719911)
	bfID_118.save()
	bmID_333,bmID_b_333 = Bookmark.objects.get_or_create(url='http://www.capitolmarkets.com/gsa-leased-investment-opportunity/')
	bmID_333.btitle='GSA Leased Opportunity Dashboard'
	bmID_333.bdescr='GSA Leased Opportunity Dashboard'
	bmID_333.save()
	bfID_333 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_333,bfrank=0.790422028851)
	bfID_333.save()
	bmID_323,bmID_b_323 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/morley-triangle/')
	bmID_323.btitle='Morley s trisector theorem'
	bmID_323.bdescr='Morley s trisector theorem'
	bmID_323.save()
	bfID_323 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_323,bfrank=0.398438556104)
	bfID_323.save()
	bmID_221,bmID_b_221 = Bookmark.objects.get_or_create(url='http://sammyd.github.com/blog/2012/09/16/visualising-conair-data-with-cubism-dot-js/')
	bmID_221.btitle='Visualising ConAir Data With Cubism js  Arduino  TempoDB  Sinatra '
	bmID_221.bdescr='Visualising ConAir Data With Cubism js  Arduino  TempoDB  Sinatra '
	bmID_221.save()
	bfID_221 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_221,bfrank=0.978691810915)
	bfID_221.save()
	bmID_215,bmID_b_215 = Bookmark.objects.get_or_create(url='http://exposedata.com/canvas/stacked.html')
	bmID_215.btitle='Canvas with d3 and Underscore'
	bmID_215.bdescr='Canvas with d3 and Underscore'
	bmID_215.save()
	bfID_215 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_215,bfrank=0.745068614469)
	bfID_215.save()
	bmID_30,bmID_b_30 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1157787')
	bmID_30.btitle='Small Multiples'
	bmID_30.bdescr='Small Multiples'
	bmID_30.save()
	bfID_30 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_30,bfrank=0.016982164534)
	bfID_30.save()
	bmID_309,bmID_b_309 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hilbert-stocks/#GOOG,AAPL,ADBE,NTFL,AMZN,INTC,ARMH,A')
	bmID_309.btitle='Hilbert Stocks'
	bmID_309.bdescr='Hilbert Stocks'
	bmID_309.save()
	bfID_309 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_309,bfrank=0.545513211832)
	bfID_309.save()
	bmID_240,bmID_b_240 = Bookmark.objects.get_or_create(url='http://fleetinbeing.net/beans/d3')
	bmID_240.btitle='A CoffeeScript console for d3 js visualization'
	bmID_240.bdescr='A CoffeeScript console for d3 js visualization'
	bmID_240.save()
	bfID_240 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_240,bfrank=0.114909224443)
	bfID_240.save()
	bmID_105,bmID_b_105 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1046712')
	bmID_105.btitle='Dependencies Between Classes'
	bmID_105.bdescr='Dependencies Between Classes'
	bmID_105.save()
	bfID_105 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_105,bfrank=0.265186872863)
	bfID_105.save()
	bmID_282,bmID_b_282 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/duplicates/')
	bmID_282.btitle='Detecting Duplicates in O 1  Space and O n  Time'
	bmID_282.bdescr='Detecting Duplicates in O 1  Space and O n  Time'
	bmID_282.save()
	bfID_282 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_282,bfrank=0.72147197586)
	bfID_282.save()
	bmID_81,bmID_b_81 = Bookmark.objects.get_or_create(url='http://fcc.github.io/calltraffic/traffic2011.html')
	bmID_81.btitle='2011 International Phone Traffic'
	bmID_81.bdescr='2011 International Phone Traffic'
	bmID_81.save()
	bfID_81 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_81,bfrank=0.938121276312)
	bfID_81.save()
	bmID_10,bmID_b_10 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-cause-patterns')
	bmID_10.btitle='GBD Cause Patterns'
	bmID_10.bdescr='GBD Cause Patterns'
	bmID_10.save()
	bfID_10 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_10,bfrank=0.455316098908)
	bfID_10.save()
	bmID_172,bmID_b_172 = Bookmark.objects.get_or_create(url='http://jklabz.com/d3/digital_clock/digital_clock.html')
	bmID_172.btitle='Digital Clock By Virtual Force'
	bmID_172.bdescr='Digital Clock By Virtual Force'
	bmID_172.save()
	bfID_172 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_172,bfrank=0.0856930014818)
	bfID_172.save()
	bmID_1,bmID_b_1 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_1.btitle='US Health Map'
	bmID_1.bdescr='US Health Map'
	bmID_1.save()
	bfID_1 = BookmarkToFolder.objects.create(bffolder=f_Evaluation_Gosel,bfbookmark=bmID_1,bfrank=0.070235477703)
	bfID_1.save()
	bmID_83,bmID_b_83 = Bookmark.objects.get_or_create(url='http://xliberation.com/googlecharts/d3nodefocustagsite.html')
	bmID_83.btitle='Navigate site by tags focus'
	bmID_83.bdescr='Navigate site by tags focus'
	bmID_83.save()
	bfID_83 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_83,bfrank=0.620023281606)
	bfID_83.save()
	bmID_99,bmID_b_99 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4092944')
	bmID_99.btitle='Circular tree of d3 src using burrow   for recursive nesting'
	bmID_99.bdescr='Circular tree of d3 src using burrow   for recursive nesting'
	bmID_99.save()
	bfID_99 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_99,bfrank=0.820105325452)
	bfID_99.save()
	bmID_338,bmID_b_338 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/nationality_by_city.html')
	bmID_338.btitle='Proportion of Foreign Born in Large Cities  1900'
	bmID_338.bdescr='Proportion of Foreign Born in Large Cities  1900'
	bmID_338.save()
	bfID_338 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_338,bfrank=0.374060871137)
	bfID_338.save()
	bmID_302,bmID_b_302 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bloomfilter/')
	bmID_302.btitle='Bloom Filters'
	bmID_302.bdescr='Bloom Filters'
	bmID_302.save()
	bfID_302 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_302,bfrank=0.648701648114)
	bfID_302.save()
	bmID_165,bmID_b_165 = Bookmark.objects.get_or_create(url='http://dan.iel.fm/xkcd/')
	bmID_165.btitle='XKCD style plots'
	bmID_165.bdescr='XKCD style plots'
	bmID_165.save()
	bfID_165 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_165,bfrank=0.887522215462)
	bfID_165.save()
	bmID_122,bmID_b_122 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1005090')
	bmID_122.btitle='Marimekko Chart'
	bmID_122.bdescr='Marimekko Chart'
	bmID_122.save()
	bfID_122 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_122,bfrank=0.0834049249876)
	bfID_122.save()
	bmID_254,bmID_b_254 = Bookmark.objects.get_or_create(url='http://nodal.me/login')
	bmID_254.btitle='Nodal is a fun way to view your GitHub network graph'
	bmID_254.bdescr='Nodal is a fun way to view your GitHub network graph'
	bmID_254.save()
	bfID_254 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_254,bfrank=0.895408781037)
	bfID_254.save()
	bmID_263,bmID_b_263 = Bookmark.objects.get_or_create(url='http://square.github.com/crossfilter/')
	bmID_263.btitle='Crossfilter'
	bmID_263.bdescr='Crossfilter'
	bmID_263.save()
	bfID_263 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_263,bfrank=0.374509153051)
	bfID_263.save()
	bmID_208,bmID_b_208 = Bookmark.objects.get_or_create(url='http://blog.nextgenetics.net/?e=7')
	bmID_208.btitle='Data visualization with D3 js and python'
	bmID_208.bdescr='Data visualization with D3 js and python'
	bmID_208.save()
	bfID_208 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_208,bfrank=0.978336169258)
	bfID_208.save()
	bmID_31,bmID_b_31 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2011/08/08/simple-sparkline-using-svg-path-and-d3-js/')
	bmID_31.btitle='Sparklines'
	bmID_31.bdescr='Sparklines'
	bmID_31.save()
	bfID_31 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_31,bfrank=0.791708636171)
	bfID_31.save()
	bmID_63,bmID_b_63 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/kerryrodden/7090426')
	bmID_63.btitle='Using a sunburst to analyze sequences of events'
	bmID_63.bdescr='Using a sunburst to analyze sequences of events'
	bmID_63.save()
	bfID_63 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_63,bfrank=0.780748659034)
	bfID_63.save()
	bmID_291,bmID_b_291 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/rhodonea/')
	bmID_291.btitle='Rhodonea Curve'
	bmID_291.bdescr='Rhodonea Curve'
	bmID_291.save()
	bfID_291 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_291,bfrank=0.265706482756)
	bfID_291.save()
	bmID_288,bmID_b_288 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/random-arboretum/')
	bmID_288.btitle='Random Arboretum'
	bmID_288.bdescr='Random Arboretum'
	bmID_288.save()
	bfID_288 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_288,bfrank=0.0380570638531)
	bfID_288.save()
	bmID_123,bmID_b_123 = Bookmark.objects.get_or_create(url='http://tomerdoron.blogspot.com/2011/12/google-style-gauges-using-d3js.html')
	bmID_123.btitle='Gauge'
	bmID_123.bdescr='Gauge'
	bmID_123.save()
	bfID_123 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_123,bfrank=0.0143275146109)
	bfID_123.save()
	bmID_91,bmID_b_91 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1093025')
	bmID_91.btitle='Indented Tree  Collapsible '
	bmID_91.bdescr='Indented Tree  Collapsible '
	bmID_91.save()
	bfID_91 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_91,bfrank=0.619901976201)
	bfID_91.save()
	bmID_319,bmID_b_319 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bifurcation/')
	bmID_319.btitle='Monte Carlo simulation of bifurcations in the logistic map'
	bmID_319.bdescr='Monte Carlo simulation of bifurcations in the logistic map'
	bmID_319.save()
	bfID_319 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_319,bfrank=0.765090704006)
	bfID_319.save()
	bmID_11,bmID_b_11 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-2010-healthy-years-lost-vs-life-expectancy')
	bmID_11.btitle='GBD 2010 healthy years lost vs life expectancy'
	bmID_11.bdescr='GBD 2010 healthy years lost vs life expectancy'
	bmID_11.save()
	bfID_11 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gosel,bfbookmark=bmID_11,bfrank=0.682592616588)
	bfID_11.save()
	bmID_124,bmID_b_124 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2011590')
	bmID_124.btitle='Chernoff faces'
	bmID_124.bdescr='Chernoff faces'
	bmID_124.save()
	bfID_124 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_124,bfrank=0.907022150593)
	bfID_124.save()
	bmID_153,bmID_b_153 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1386444')
	bmID_153.btitle='Square Circle Spiral Illusion'
	bmID_153.bdescr='Square Circle Spiral Illusion'
	bmID_153.save()
	bfID_153 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_153,bfrank=0.569945503045)
	bfID_153.save()
	bmID_160,bmID_b_160 = Bookmark.objects.get_or_create(url='http://blog.latentflip.com/post/18195267992/d3-collider')
	bmID_160.btitle='Collider   a d3 js game'
	bmID_160.bdescr='Collider   a d3 js game'
	bmID_160.save()
	bfID_160 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_160,bfrank=0.406382167245)
	bfID_160.save()
	bmID_42,bmID_b_42 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1305111')
	bmID_42.btitle='Pie Multiples'
	bmID_42.bdescr='Pie Multiples'
	bmID_42.save()
	bfID_42 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gosel,bfbookmark=bmID_42,bfrank=0.765897313181)
	bfID_42.save()
	bmID_328,bmID_b_328 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/american-forces-in-afghanistan-and-iraq/')
	bmID_328.btitle='American Forces in Afghanistan and Iraq'
	bmID_328.bdescr='American Forces in Afghanistan and Iraq'
	bmID_328.save()
	bfID_328 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_328,bfrank=0.303867848826)
	bfID_328.save()
	bmID_289,bmID_b_289 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/crayola/')
	bmID_289.btitle='Crayola Colour Chronology'
	bmID_289.bdescr='Crayola Colour Chronology'
	bmID_289.save()
	bfID_289 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_289,bfrank=0.149894647729)
	bfID_289.save()
	bmID_303,bmID_b_303 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/carotid/')
	bmID_303.btitle='Carotid Kundalini Fractal Explorer'
	bmID_303.bdescr='Carotid Kundalini Fractal Explorer'
	bmID_303.save()
	bfID_303 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_303,bfrank=0.175807495098)
	bfID_303.save()
	bmID_32,bmID_b_32 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2012/05/15/interactive-line-graph-using-d3-js/')
	bmID_32.btitle='Interactive Line Graph'
	bmID_32.bdescr='Interactive Line Graph'
	bmID_32.save()
	bfID_32 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_32,bfrank=0.886265660901)
	bfID_32.save()
	bmID_58,bmID_b_58 = Bookmark.objects.get_or_create(url='http://charts.graphicbaseball.com/parallelbatting')
	bmID_58.btitle='Graphicbaseball  2012 Batters'
	bmID_58.bdescr='Graphicbaseball  2012 Batters'
	bmID_58.save()
	bfID_58 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Wen,bfbookmark=bmID_58,bfrank=0.549558879124)
	bfID_58.save()
	bmID_331,bmID_b_331 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/gates/')
	bmID_331.btitle='Animated Bubble Chart of Gates Educational Donations'
	bmID_331.bdescr='Animated Bubble Chart of Gates Educational Donations'
	bmID_331.save()
	bfID_331 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_331,bfrank=0.413903525252)
	bfID_331.save()
	bmID_321,bmID_b_321 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/complete-graphs/')
	bmID_321.btitle='Complete Graphs'
	bmID_321.bdescr='Complete Graphs'
	bmID_321.save()
	bfID_321 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_321,bfrank=0.0385080405089)
	bfID_321.save()
	bmID_183,bmID_b_183 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/shawnbot/BJLe6/')
	bmID_183.btitle='Responsive SVG resizing without re rendering'
	bmID_183.bdescr='Responsive SVG resizing without re rendering'
	bmID_183.save()
	bfID_183 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_183,bfrank=0.33169760927)
	bfID_183.save()
	bmID_226,bmID_b_226 = Bookmark.objects.get_or_create(url='http://briantford.com/blog/angular-d3.html')
	bmID_226.btitle='Using the D3 js Visualization Library with AngularJS'
	bmID_226.bdescr='Using the D3 js Visualization Library with AngularJS'
	bmID_226.save()
	bfID_226 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_226,bfrank=0.527382647348)
	bfID_226.save()
	bmID_67,bmID_b_67 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2920551')
	bmID_67.btitle='Multi Foci with Convex Hulls'
	bmID_67.bdescr='Multi Foci with Convex Hulls'
	bmID_67.save()
	bfID_67 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_67,bfrank=0.480644714267)
	bfID_67.save()
	bmID_306,bmID_b_306 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-quasicrystals/')
	bmID_306.btitle='Animated Quasicrystals'
	bmID_306.bdescr='Animated Quasicrystals'
	bmID_306.save()
	bfID_306 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_306,bfrank=0.199089037445)
	bfID_306.save()
	bmID_225,bmID_b_225 = Bookmark.objects.get_or_create(url='https://github.com/hadley/r2d3')
	bmID_225.btitle='ggplot2   d3   r2d3'
	bmID_225.bdescr='ggplot2   d3   r2d3'
	bmID_225.save()
	bfID_225 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_225,bfrank=0.948014906152)
	bfID_225.save()
	bmID_104,bmID_b_104 = Bookmark.objects.get_or_create(url='http://www.torre.nl/remittances/')
	bmID_104.btitle='Remittance flows'
	bmID_104.bdescr='Remittance flows'
	bmID_104.save()
	bfID_104 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_104,bfrank=0.597577583623)
	bfID_104.save()
	bmID_48,bmID_b_48 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4481531')
	bmID_48.btitle='Scatterplot  Social trust vs ease of doing business'
	bmID_48.bdescr='Scatterplot  Social trust vs ease of doing business'
	bmID_48.save()
	bfID_48 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gosel,bfbookmark=bmID_48,bfrank=0.0271668881171)
	bfID_48.save()
	bmID_228,bmID_b_228 = Bookmark.objects.get_or_create(url='http://jllord.github.com/sheetsee.js/')
	bmID_228.btitle='SHEETSEE JS  Fill up Websites with Stuff from Google Spreasheet'
	bmID_228.bdescr='SHEETSEE JS  Fill up Websites with Stuff from Google Spreasheet'
	bmID_228.save()
	bfID_228 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_228,bfrank=0.627387624935)
	bfID_228.save()
	bmID_134,bmID_b_134 = Bookmark.objects.get_or_create(url='http://mohdaslam.com/lte-rrc-rlc-mac-visualization-using-bubble-pack-layout/')
	bmID_134.btitle='LTE Protocol visualization'
	bmID_134.bdescr='LTE Protocol visualization'
	bmID_134.save()
	bfID_134 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_134,bfrank=0.503973912892)
	bfID_134.save()
	bmID_257,bmID_b_257 = Bookmark.objects.get_or_create(url='http://mortgagebloom.com')
	bmID_257.btitle='MortgageBloom Calculator'
	bmID_257.bdescr='MortgageBloom Calculator'
	bmID_257.save()
	bfID_257 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_257,bfrank=0.0256618367432)
	bfID_257.save()
	bmID_176,bmID_b_176 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1503463')
	bmID_176.btitle='Masking with external svg elements'
	bmID_176.bdescr='Masking with external svg elements'
	bmID_176.save()
	bfID_176 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_176,bfrank=0.308044113979)
	bfID_176.save()
	bmID_230,bmID_b_230 = Bookmark.objects.get_or_create(url='http://dexvis.com')
	bmID_230.btitle='Dex the Data Explorer'
	bmID_230.bdescr='Dex the Data Explorer'
	bmID_230.save()
	bfID_230 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_230,bfrank=0.0168554888404)
	bfID_230.save()
	bmID_84,bmID_b_84 = Bookmark.objects.get_or_create(url='http://blog.pixelingene.com/2011/07/building-a-tree-diagram-in-d3-js/')
	bmID_84.btitle='Building a tree diagram'
	bmID_84.bdescr='Building a tree diagram'
	bmID_84.save()
	bfID_84 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_84,bfrank=0.466822697905)
	bfID_84.save()
	bmID_116,bmID_b_116 = Bookmark.objects.get_or_create(url='http://radialsets.org')
	bmID_116.btitle='Visualizing Overlapping Sets'
	bmID_116.bdescr='Visualizing Overlapping Sets'
	bmID_116.save()
	bfID_116 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_116,bfrank=0.680195324925)
	bfID_116.save()
	bmID_146,bmID_b_146 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1098617')
	bmID_146.btitle='Arc Tweens'
	bmID_146.bdescr='Arc Tweens'
	bmID_146.save()
	bfID_146 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_146,bfrank=0.0685299507851)
	bfID_146.save()
	bmID_279,bmID_b_279 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/simplify/koch/')
	bmID_279.btitle='Quadratic Koch Island Simplification'
	bmID_279.bdescr='Quadratic Koch Island Simplification'
	bmID_279.save()
	bfID_279 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_279,bfrank=0.967703527981)
	bfID_279.save()
	bmID_139,bmID_b_139 = Bookmark.objects.get_or_create(url='http://ggruiz.me/weeknd3/')
	bmID_139.btitle='Weeknd3'
	bmID_139.bdescr='Weeknd3'
	bmID_139.save()
	bfID_139 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_139,bfrank=0.972576851521)
	bfID_139.save()
	bmID_74,bmID_b_74 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1153292')
	bmID_74.btitle='Directed Edges  Curves and Arrow Markers '
	bmID_74.bdescr='Directed Edges  Curves and Arrow Markers '
	bmID_74.save()
	bfID_74 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_74,bfrank=0.707719557743)
	bfID_74.save()
	bmID_70,bmID_b_70 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/929623')
	bmID_70.btitle='Interactive Construction'
	bmID_70.bdescr='Interactive Construction'
	bmID_70.save()
	bfID_70 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_70,bfrank=0.301320414449)
	bfID_70.save()
	bmID_202,bmID_b_202 = Bookmark.objects.get_or_create(url='http://quasipartikel.at/2012/04/25/dancing-with-data/')
	bmID_202.btitle='Dance js  D3 with Backbone and Data js'
	bmID_202.bdescr='Dance js  D3 with Backbone and Data js'
	bmID_202.save()
	bfID_202 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_202,bfrank=0.283775692357)
	bfID_202.save()
	bmID_318,bmID_b_318 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/apollonian-gasket/')
	bmID_318.btitle='Apollonian Gasket'
	bmID_318.bdescr='Apollonian Gasket'
	bmID_318.save()
	bfID_318 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_318,bfrank=0.265236349602)
	bfID_318.save()
	bmID_293,bmID_b_293 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/necklaces/')
	bmID_293.btitle='Combinatorial Necklaces and Bracelets'
	bmID_293.bdescr='Combinatorial Necklaces and Bracelets'
	bmID_293.save()
	bfID_293 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_293,bfrank=0.641468666645)
	bfID_293.save()
	bmID_287,bmID_b_287 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/plasma/')
	bmID_287.btitle='Infinite Plasma Fractal'
	bmID_287.bdescr='Infinite Plasma Fractal'
	bmID_287.save()
	bfID_287 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_287,bfrank=0.356203361378)
	bfID_287.save()
	bmID_5,bmID_b_5 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/mortality/')
	bmID_5.btitle='Mortality Visualization'
	bmID_5.bdescr='Mortality Visualization'
	bmID_5.save()
	bfID_5 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gosel,bfbookmark=bmID_5,bfrank=0.982709007539)
	bfID_5.save()
	bmID_211,bmID_b_211 = Bookmark.objects.get_or_create(url='http://excelramblings.blogspot.co.uk/2012/07/visualizing-system-integrations-using.html')
	bmID_211.btitle='d3 js force diagrams with markers straight from Excel'
	bmID_211.bdescr='d3 js force diagrams with markers straight from Excel'
	bmID_211.save()
	bfID_211 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_211,bfrank=0.218681163204)
	bfID_211.save()
	bmID_87,bmID_b_87 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2966094')
	bmID_87.btitle='Pedigree Tree'
	bmID_87.bdescr='Pedigree Tree'
	bmID_87.save()
	bfID_87 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_87,bfrank=0.482345664534)
	bfID_87.save()
	bmID_298,bmID_b_298 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/mobile-lawsuits/')
	bmID_298.btitle='Mobile Patent Lawsuits'
	bmID_298.bdescr='Mobile Patent Lawsuits'
	bmID_298.save()
	bfID_298 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_298,bfrank=0.813246495843)
	bfID_298.save()
	bmID_201,bmID_b_201 = Bookmark.objects.get_or_create(url='https://github.com/hhuuggoo/pushd3')
	bmID_201.btitle='Pushing d3 commands to the browser from iPython'
	bmID_201.bdescr='Pushing d3 commands to the browser from iPython'
	bmID_201.save()
	bfID_201 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_201,bfrank=0.231392837336)
	bfID_201.save()
	bmID_128,bmID_b_128 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/d/3779574/')
	bmID_128.btitle='Sankey Diagram with Overlap'
	bmID_128.bdescr='Sankey Diagram with Overlap'
	bmID_128.save()
	bfID_128 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_128,bfrank=0.566062020291)
	bfID_128.save()
	bmID_198,bmID_b_198 = Bookmark.objects.get_or_create(url='https://github.com/mikedewar/d3py')
	bmID_198.btitle='Plotting library for python based on d3'
	bmID_198.bdescr='Plotting library for python based on d3'
	bmID_198.save()
	bfID_198 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_198,bfrank=0.565154821449)
	bfID_198.save()
	bmID_325,bmID_b_325 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/pythagoras-proof/')
	bmID_325.btitle='Proof of Pythagoras  Theorem'
	bmID_325.bdescr='Proof of Pythagoras  Theorem'
	bmID_325.save()
	bfID_325 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_325,bfrank=0.190076321497)
	bfID_325.save()
	bmID_267,bmID_b_267 = Bookmark.objects.get_or_create(url='http://www.visualsedimentation.org/')
	bmID_267.btitle='VisualSedimentation js  visualizing streaming data  inspired by the process of physical sedimentation'
	bmID_267.bdescr='VisualSedimentation js  visualizing streaming data  inspired by the process of physical sedimentation'
	bmID_267.save()
	bfID_267 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_267,bfrank=0.713604309058)
	bfID_267.save()
	bmID_154,bmID_b_154 = Bookmark.objects.get_or_create(url='https://github.com/enjalot/adventures_in_d3')
	bmID_154.btitle='Adventures in D3'
	bmID_154.bdescr='Adventures in D3'
	bmID_154.save()
	bfID_154 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_154,bfrank=0.310411437199)
	bfID_154.save()
	bmID_196,bmID_b_196 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4149176')
	bmID_196.btitle='Custom Multi Scale Time Format Axis'
	bmID_196.bdescr='Custom Multi Scale Time Format Axis'
	bmID_196.save()
	bfID_196 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_196,bfrank=0.173545201578)
	bfID_196.save()
	bmID_290,bmID_b_290 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/parallel-sets/')
	bmID_290.btitle='Parallel Sets'
	bmID_290.bdescr='Parallel Sets'
	bmID_290.save()
	bfID_290 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_290,bfrank=0.271529164497)
	bfID_290.save()
	bmID_145,bmID_b_145 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1182434')
	bmID_145.btitle='Spline  Zoom and Pan'
	bmID_145.bdescr='Spline  Zoom and Pan'
	bmID_145.save()
	bfID_145 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_145,bfrank=0.741842486929)
	bfID_145.save()
	bmID_77,bmID_b_77 = Bookmark.objects.get_or_create(url='http://www.torlaune.de/euro-2012/spieler-relationen/')
	bmID_77.btitle='Groups and Labels showing relations of football players participating in Euro 2012'
	bmID_77.bdescr='Groups and Labels showing relations of football players participating in Euro 2012'
	bmID_77.save()
	bfID_77 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_77,bfrank=0.190662982656)
	bfID_77.save()
	bmID_79,bmID_b_79 = Bookmark.objects.get_or_create(url='http://fanfarefantastique.com/vishna/')
	bmID_79.btitle='Hacker News Visualisation'
	bmID_79.bdescr='Hacker News Visualisation'
	bmID_79.save()
	bfID_79 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_79,bfrank=0.0775733107164)
	bfID_79.save()
	bmID_189,bmID_b_189 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4047002')
	bmID_189.btitle='Custom Path and Area Generator'
	bmID_189.bdescr='Custom Path and Area Generator'
	bmID_189.save()
	bfID_189 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_189,bfrank=0.418996906379)
	bfID_189.save()
	bmID_162,bmID_b_162 = Bookmark.objects.get_or_create(url='http://markmarkoh.com/rhok')
	bmID_162.btitle='Conway s Game of life as a scrolling background'
	bmID_162.bdescr='Conway s Game of life as a scrolling background'
	bmID_162.save()
	bfID_162 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_162,bfrank=0.55861815511)
	bfID_162.save()
	bmID_151,bmID_b_151 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1276463')
	bmID_151.btitle='DOM to Canvas'
	bmID_151.bdescr='DOM to Canvas'
	bmID_151.save()
	bfID_151 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_151,bfrank=0.64002484781)
	bfID_151.save()
	bmID_133,bmID_b_133 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1020902')
	bmID_133.btitle='Superformula Tweening'
	bmID_133.bdescr='Superformula Tweening'
	bmID_133.save()
	bfID_133 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_133,bfrank=0.0473998443513)
	bfID_133.save()
	bmID_322,bmID_b_322 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/leibniz-spiral/')
	bmID_322.btitle='Leibniz Spiral'
	bmID_322.bdescr='Leibniz Spiral'
	bmID_322.save()
	bfID_322 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_322,bfrank=0.391101244499)
	bfID_322.save()
	bmID_34,bmID_b_34 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2012/05/02/line-graphs-using-d3-js/')
	bmID_34.btitle='Dual scale line chart'
	bmID_34.bdescr='Dual scale line chart'
	bmID_34.save()
	bfID_34 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_34,bfrank=0.570221548049)
	bfID_34.save()
	bmID_39,bmID_b_39 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4175202')
	bmID_39.btitle='Multiple time series with object constancy'
	bmID_39.bdescr='Multiple time series with object constancy'
	bmID_39.save()
	bfID_39 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gosel,bfbookmark=bmID_39,bfrank=0.518709883315)
	bfID_39.save()

	#Bin Folders
	binID_0 = add_binfolder(busername_fk=Martyna)
	binID_1 = add_binfolder(busername_fk=James)
	binID_2 = add_binfolder(busername_fk=Jean)
	binID_3 = add_binfolder(busername_fk=Wen)
	binID_4 = add_binfolder(busername_fk=Gosel)

def add_bookmark(url, btitle, bdescr, bdomain, fname, saved_times=0):
	bm = Bookmark.objects.get_or_create(url=url, btitle=btitle, bdescr=bdescr, bdomain=bdomain, fname=fname, saved_times=saved_times)[0]
	return bm

def add_folder(foldername, fusername_fk):
	f = Folder.objects.get_or_create(foldername=foldername, fusername_fk=fusername_fk)[0]
	return f

def add_binfolder(busername_fk):
	bf = BinFolder.objects.get_or_create(busername_fk=busername_fk)[0]
	return bf

# Start execution here!
if __name__ == '__main__':
	print 'Starting DragonDrop population script...'
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dragondrop_proj.settings')
	from dragondrop.models import User, Bookmark, Folder, BinFolder, BookmarkToFolder 
	populate()
