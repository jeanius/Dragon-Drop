import os
import dragondrop.get_domain_from_url

def populate():

	#Users
	Jean = User.objects.create_user('Jean',None, 'Jeanpassword')
	Jean.save()
	Wen = User.objects.create_user('Wen',None, 'Wenpassword')
	Wen.save()
	Gozel = User.objects.create_user('Gozel',None, 'Gozelpassword')
	Gozel.save()
	James = User.objects.create_user('James',None, 'Jamespassword')
	James.save()
	Martyna = User.objects.create_user('Martyna',None, 'Martynapassword')
	Martyna.save()
	Leif = User.objects.create_user('Leif',None, 'Leifpassword')
	James.save()

	#Folders
	f_Misc_Trees_and_Graphs_Wen = add_folder(foldername='Misc Trees and Graphs',fusername_fk=Wen)
	f_Online_Editors_Jean = add_folder(foldername='Online Editors',fusername_fk=Jean)
	f_Misc_Charts_Jean = add_folder(foldername='Misc Charts',fusername_fk=Jean)
	f_Online_Editors_Martyna = add_folder(foldername='Online Editors',fusername_fk=Martyna)
	f_Sunburst_and_Partition_layout_Wen = add_folder(foldername='Sunburst and Partition layout',fusername_fk=Wen)
	f_Useful_snippets_Jean = add_folder(foldername='Useful snippets',fusername_fk=Jean)
	f_Miscellaneous_visualizations_Jean = add_folder(foldername='Miscellaneous visualizations',fusername_fk=Jean)
	f_Tree_Wen = add_folder(foldername='Tree',fusername_fk=Wen)
	f_Jason_Davies_James = add_folder(foldername='Jason Davies',fusername_fk=James)
	f_Scatterplot_and_Bubble_chart_Gozel = add_folder(foldername='Scatterplot and Bubble chart',fusername_fk=Gozel)
	f_Products_Martyna = add_folder(foldername='Products',fusername_fk=Martyna)
	f_Institute_for_Health_Metrics_and_Evaluation_Gozel = add_folder(foldername='Institute for Health Metrics and Evaluation',fusername_fk=Gozel)
	f_Maps_Jean = add_folder(foldername='Maps',fusername_fk=Jean)
	f_Jim_Vallandingham_James = add_folder(foldername='Jim Vallandingham',fusername_fk=James)
	f_Chord_Layout_Jean = add_folder(foldername='Chord Layout',fusername_fk=Jean)
	f_Store_Apps_Martyna = add_folder(foldername='Store Apps',fusername_fk=Martyna)
	f_Force_Layout_Wen = add_folder(foldername='Force Layout',fusername_fk=Wen)
	f_Miscellaneous_visualizations_Gozel = add_folder(foldername='Miscellaneous visualizations',fusername_fk=Gozel)
	f_Libraries_Martyna = add_folder(foldername='Libraries',fusername_fk=Martyna)
	f_Pie_Chart_Gozel = add_folder(foldername='Pie Chart',fusername_fk=Gozel)
	f_Bar_Chart_Gozel = add_folder(foldername='Bar Chart',fusername_fk=Gozel)
	f_Maps_Gozel = add_folder(foldername='Maps',fusername_fk=Gozel)
	f_Histogram_Gozel = add_folder(foldername='Histogram',fusername_fk=Gozel)
	f_Line_and_Area_Chart_Gozel = add_folder(foldername='Line and Area Chart',fusername_fk=Gozel)
	f_Jerome_Cukier_Martyna = add_folder(foldername='Jerome Cukier',fusername_fk=Martyna)
	f_Chord_Layout_Wen = add_folder(foldername='Chord Layout',fusername_fk=Wen)
	f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel = add_folder(foldername='Parallel Coordinates Parallel sets and Sankey',fusername_fk=Gozel)
	f_Jason_Davies_Martyna = add_folder(foldername='Jason Davies',fusername_fk=Martyna)
	f_Interoperability_Jean = add_folder(foldername='Interoperability',fusername_fk=Jean)
	f_Parallel_Coordinates_Parallel_sets_and_Sankey_Wen = add_folder(foldername='Parallel Coordinates Parallel sets and Sankey',fusername_fk=Wen)

	#Bookmarks
	bmID_178,bmID_b_178 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3310323')
	bmID_178.btitle='Custom Line Interpolation'
	bmID_178.bdescr='Custom Line Interpolation'
	bmID_178.save()
	bfID_178 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_178,bfrank=0.637775240533,clicks=11)
	bfID_178.save()
	bmID_213,bmID_b_213 = Bookmark.objects.get_or_create(url='http://css.dzone.com/articles/render-geographic-information')
	bmID_213.btitle='Render Geographic Information in 3D With Three js and D3 js'
	bmID_213.bdescr='Render Geographic Information in 3D With Three js and D3 js'
	bmID_213.save()
	bfID_213 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_213,bfrank=0.145732154088,clicks=70)
	bfID_213.save()
	bmID_58,bmID_b_58 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/coffee-wheel/')
	bmID_58.btitle='Sunburst  Coffee Flavour Wheel'
	bmID_58.bdescr='Sunburst  Coffee Flavour Wheel'
	bmID_58.save()
	bfID_58 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_58,bfrank=0.28187953458,clicks=15)
	bfID_58.save()
	bmID_59,bmID_b_59 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1005873')
	bmID_59.btitle='Partition Layout  Zoomable Icicle '
	bmID_59.bdescr='Partition Layout  Zoomable Icicle '
	bmID_59.save()
	bfID_59 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_59,bfrank=0.953667702329,clicks=73)
	bfID_59.save()
	bmID_194,bmID_b_194 = Bookmark.objects.get_or_create(url='http://drsm79.github.com/Backbone-d3/index.html')
	bmID_194.btitle='Backbone D3'
	bmID_194.bdescr='Backbone D3'
	bmID_194.save()
	bfID_194 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_194,bfrank=0.329418092172,clicks=40)
	bfID_194.save()
	bmID_278,bmID_b_278 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/plasma/')
	bmID_278.btitle='Infinite Plasma Fractal'
	bmID_278.bdescr='Infinite Plasma Fractal'
	bmID_278.save()
	bfID_278 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_278,bfrank=0.787354275638,clicks=39)
	bfID_278.save()
	bmID_177,bmID_b_177 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/3689677')
	bmID_177.btitle='Long Scroll'
	bmID_177.bdescr='Long Scroll'
	bmID_177.save()
	bfID_177 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_177,bfrank=0.589763298709,clicks=83)
	bfID_177.save()
	bmID_149,bmID_b_149 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1405439')
	bmID_149.btitle='Voronoi based point picker'
	bmID_149.bdescr='Voronoi based point picker'
	bmID_149.save()
	bfID_149 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_149,bfrank=0.924711039347,clicks=65)
	bfID_149.save()
	bmID_305,bmID_b_305 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/tree-of-life/')
	bmID_305.btitle='Phylogenetic Tree of Life'
	bmID_305.bdescr='Phylogenetic Tree of Life'
	bmID_305.save()
	bfID_305 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_305,bfrank=0.599815045136,clicks=46)
	bfID_305.save()
	bmID_225,bmID_b_225 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/gassites/d3-concept-browser')
	bmID_225.btitle='Force directed site concept browser'
	bmID_225.bdescr='Force directed site concept browser'
	bmID_225.save()
	bfID_225 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_225,bfrank=0.270178457835,clicks=93)
	bfID_225.save()
	bmID_87,bmID_b_87 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1061834')
	bmID_87.btitle='Collapsible'
	bmID_87.bdescr='Collapsible'
	bmID_87.save()
	bfID_87 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_87,bfrank=0.638365491119,clicks=93)
	bfID_87.save()
	bmID_109,bmID_b_109 = Bookmark.objects.get_or_create(url='http://radialsets.org')
	bmID_109.btitle='Visualizing Overlapping Sets'
	bmID_109.bdescr='Visualizing Overlapping Sets'
	bmID_109.save()
	bfID_109 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_109,bfrank=0.946359195593,clicks=54)
	bfID_109.save()
	bmID_205,bmID_b_205 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/plaliberte/HAXyd/')
	bmID_205.btitle='SVG to Canvas to PNG using Canvg'
	bmID_205.bdescr='SVG to Canvas to PNG using Canvg'
	bmID_205.save()
	bfID_205 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_205,bfrank=0.676703274687,clicks=78)
	bfID_205.save()
	bmID_239,bmID_b_239 = Bookmark.objects.get_or_create(url='http://plot.io/')
	bmID_239.btitle='Plot io  swallowed by Platfora '
	bmID_239.bdescr='Plot io  swallowed by Platfora '
	bmID_239.save()
	bfID_239 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_239,bfrank=0.0183769171904,clicks=96)
	bfID_239.save()
	bmID_155,bmID_b_155 = Bookmark.objects.get_or_create(url='http://markmarkoh.com/rhok')
	bmID_155.btitle='Conway s Game of life as a scrolling background'
	bmID_155.bdescr='Conway s Game of life as a scrolling background'
	bmID_155.save()
	bfID_155 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_155,bfrank=0.260737238234,clicks=63)
	bfID_155.save()
	bmID_95,bmID_b_95 = Bookmark.objects.get_or_create(url='http://bit.ly/PvWgUH')
	bmID_95.btitle='SCION simulation environment'
	bmID_95.bdescr='SCION simulation environment'
	bmID_95.save()
	bfID_95 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_95,bfrank=0.184273943707,clicks=86)
	bfID_95.save()
	bmID_88,bmID_b_88 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1249394')
	bmID_88.btitle='Collapsible  with Labels'
	bmID_88.bdescr='Collapsible  with Labels'
	bmID_88.save()
	bfID_88 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_88,bfrank=0.655181353785,clicks=51)
	bfID_88.save()
	bmID_27,bmID_b_27 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1166403')
	bmID_27.btitle='Axis Component'
	bmID_27.bdescr='Axis Component'
	bmID_27.save()
	bfID_27 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_27,bfrank=0.793551443791,clicks=28)
	bfID_27.save()
	bmID_24,bmID_b_24 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3048450')
	bmID_24.btitle='Fixed width Histogram  Irwin Hall distribution'
	bmID_24.bdescr='Fixed width Histogram  Irwin Hall distribution'
	bmID_24.save()
	bfID_24 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gozel,bfbookmark=bmID_24,bfrank=0.591742330188,clicks=5)
	bfID_24.save()
	bmID_288,bmID_b_288 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/planarity/')
	bmID_288.btitle='Planarity'
	bmID_288.bdescr='Planarity'
	bmID_288.save()
	bfID_288 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_288,bfrank=0.3657918488,clicks=5)
	bfID_288.save()
	bmID_57,bmID_b_57 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/910126')
	bmID_57.btitle='Sunburst Layout with Labels'
	bmID_57.bdescr='Sunburst Layout with Labels'
	bmID_57.save()
	bfID_57 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_57,bfrank=0.996955830445,clicks=54)
	bfID_57.save()
	bmID_38,bmID_b_38 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/nswamy14/083a1e3181c81428f817')
	bmID_38.btitle='Overlapped distribution Area chart'
	bmID_38.bdescr='Overlapped distribution Area chart'
	bmID_38.save()
	bfID_38 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_38,bfrank=0.725620610323,clicks=93)
	bfID_38.save()
	bmID_203,bmID_b_203 = Bookmark.objects.get_or_create(url='http://www.benh.co.uk/datasift/visualising-a-datasift-feed-with-node-and-d3/')
	bmID_203.btitle='Visualising a real time DataSift feed with Node and D3 js'
	bmID_203.bdescr='Visualising a real time DataSift feed with Node and D3 js'
	bmID_203.save()
	bfID_203 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_203,bfrank=0.736573821974,clicks=9)
	bfID_203.save()
	bmID_290,bmID_b_290 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/sunflower-phyllotaxis/')
	bmID_290.btitle='Sunflower Phyllotaxis'
	bmID_290.bdescr='Sunflower Phyllotaxis'
	bmID_290.save()
	bfID_290 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_290,bfrank=0.14543032394,clicks=84)
	bfID_290.save()
	bmID_284,bmID_b_284 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/necklaces/')
	bmID_284.btitle='Combinatorial Necklaces and Bracelets'
	bmID_284.bdescr='Combinatorial Necklaces and Bracelets'
	bmID_284.save()
	bfID_284 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_284,bfrank=0.934947693474,clicks=30)
	bfID_284.save()
	bmID_219,bmID_b_219 = Bookmark.objects.get_or_create(url='http://jllord.github.com/sheetsee.js/')
	bmID_219.btitle='SHEETSEE JS  Fill up Websites with Stuff from Google Spreasheet'
	bmID_219.bdescr='SHEETSEE JS  Fill up Websites with Stuff from Google Spreasheet'
	bmID_219.save()
	bfID_219 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_219,bfrank=0.1185585596,clicks=50)
	bfID_219.save()
	bmID_292,bmID_b_292 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/calkin-wilf-tree/')
	bmID_292.btitle='Calkin Wilf Tree'
	bmID_292.bdescr='Calkin Wilf Tree'
	bmID_292.save()
	bfID_292 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_292,bfrank=0.334783590656,clicks=14)
	bfID_292.save()
	bmID_190,bmID_b_190 = Bookmark.objects.get_or_create(url='http://github.com/jakevdp/mpld3')
	bmID_190.btitle='mpld3  d3 visualizations of matplotlib  python  plots'
	bmID_190.bdescr='mpld3  d3 visualizations of matplotlib  python  plots'
	bmID_190.save()
	bfID_190 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_190,bfrank=0.0104815109926,clicks=16)
	bfID_190.save()
	bmID_19,bmID_b_19 = Bookmark.objects.get_or_create(url='https://github.com/gencay/stackedGroupedChart')
	bmID_19.btitle='Grouped and Stacked Bar Chart'
	bmID_19.bdescr='Grouped and Stacked Bar Chart'
	bmID_19.save()
	bfID_19 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_19,bfrank=0.429233335484,clicks=58)
	bfID_19.save()
	bmID_166,bmID_b_166 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/nbremer/raw/6506614/')
	bmID_166.btitle='Radar Chart or Spider Chart'
	bmID_166.bdescr='Radar Chart or Spider Chart'
	bmID_166.save()
	bfID_166 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_166,bfrank=0.246045014534,clicks=85)
	bfID_166.save()
	bmID_263,bmID_b_263 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/percolate.html')
	bmID_263.btitle='Percolation model'
	bmID_263.bdescr='Percolation model'
	bmID_263.save()
	bfID_263 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_263,bfrank=0.254267586572,clicks=94)
	bfID_263.save()
	bmID_259,bmID_b_259 = Bookmark.objects.get_or_create(url='https://github.com/ignacioola/insights')
	bmID_259.btitle='Insights  Interactive Force Graph Component'
	bmID_259.bdescr='Insights  Interactive Force Graph Component'
	bmID_259.save()
	bfID_259 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_259,bfrank=0.97461721242,clicks=13)
	bfID_259.save()
	bmID_253,bmID_b_253 = Bookmark.objects.get_or_create(url='http://square.github.com/cubism/')
	bmID_253.btitle='Cubism js  Time Series Visualization'
	bmID_253.bdescr='Cubism js  Time Series Visualization'
	bmID_253.save()
	bfID_253 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_253,bfrank=0.121035044584,clicks=1)
	bfID_253.save()
	bmID_150,bmID_b_150 = Bookmark.objects.get_or_create(url='http://www.larsko.org/v/euc/')
	bmID_150.btitle='Radar chart'
	bmID_150.bdescr='Radar chart'
	bmID_150.save()
	bfID_150 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_150,bfrank=0.648553954856,clicks=39)
	bfID_150.save()
	bmID_42,bmID_b_42 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/4710330/94a7c0aeb6f09d681dbfdd0e5150578e4935c6ae')
	bmID_42.btitle='Hierarchical Pie Chart'
	bmID_42.bdescr='Hierarchical Pie Chart'
	bmID_42.save()
	bfID_42 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gozel,bfbookmark=bmID_42,bfrank=0.576387876383,clicks=4)
	bfID_42.save()
	bmID_202,bmID_b_202 = Bookmark.objects.get_or_create(url='http://excelramblings.blogspot.co.uk/2012/07/visualizing-system-integrations-using.html')
	bmID_202.btitle='d3 js force diagrams with markers straight from Excel'
	bmID_202.bdescr='d3 js force diagrams with markers straight from Excel'
	bmID_202.save()
	bfID_202 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_202,bfrank=0.110134665982,clicks=70)
	bfID_202.save()
	bmID_182,bmID_b_182 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3605124')
	bmID_182.btitle='Axis Examples'
	bmID_182.bdescr='Axis Examples'
	bmID_182.save()
	bfID_182 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_182,bfrank=0.388166235633,clicks=26)
	bfID_182.save()
	bmID_70,bmID_b_70 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1080941')
	bmID_70.btitle='From XML'
	bmID_70.bdescr='From XML'
	bmID_70.save()
	bfID_70 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_70,bfrank=0.656399769953,clicks=76)
	bfID_70.save()
	bmID_298,bmID_b_298 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/collatz-graph/')
	bmID_298.btitle='Collatz Graph  All Numbers Lead to One'
	bmID_298.bdescr='Collatz Graph  All Numbers Lead to One'
	bmID_298.save()
	bfID_298 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_298,bfrank=0.987718736084,clicks=2)
	bfID_298.save()
	bmID_235,bmID_b_235 = Bookmark.objects.get_or_create(url='https://bitdeli.com/')
	bmID_235.btitle='Bitdeli  Custom analytics with Python and GitHub'
	bmID_235.bdescr='Bitdeli  Custom analytics with Python and GitHub'
	bmID_235.save()
	bfID_235 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_235,bfrank=0.580114995637,clicks=61)
	bfID_235.save()
	bmID_2,bmID_b_2 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/gbd-compare/')
	bmID_2.btitle='GBD Compare'
	bmID_2.bdescr='GBD Compare'
	bmID_2.save()
	bfID_2 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gozel,bfbookmark=bmID_2,bfrank=0.510098022503,clicks=63)
	bfID_2.save()
	bmID_126,bmID_b_126 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1020902')
	bmID_126.btitle='Superformula Tweening'
	bmID_126.bdescr='Superformula Tweening'
	bmID_126.save()
	bfID_126 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_126,bfrank=0.891388265012,clicks=92)
	bfID_126.save()
	bmID_131,bmID_b_131 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/849853')
	bmID_131.btitle='Raindrops'
	bmID_131.bdescr='Raindrops'
	bmID_131.save()
	bfID_131 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_131,bfrank=0.395289444874,clicks=86)
	bfID_131.save()
	bmID_17,bmID_b_17 = Bookmark.objects.get_or_create(url='https://github.com/mlarocca/Dynamic-Charts')
	bmID_17.btitle='Dynamic Bar Charts'
	bmID_17.bdescr='Dynamic Bar Charts'
	bmID_17.save()
	bfID_17 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_17,bfrank=0.882144838989,clicks=48)
	bfID_17.save()
	bmID_130,bmID_b_130 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1117287')
	bmID_130.btitle='Segmented Lines and Slope Coloring'
	bmID_130.bdescr='Segmented Lines and Slope Coloring'
	bmID_130.save()
	bfID_130 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_130,bfrank=0.545495742218,clicks=83)
	bfID_130.save()
	bmID_0,bmID_b_0 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_0.btitle='US Health Map'
	bmID_0.bdescr='US Health Map'
	bmID_0.save()
	bfID_0 = BookmarkToFolder.objects.create(bffolder=f_Maps_Gozel,bfbookmark=bmID_0,bfrank=0.571273576017,clicks=11)
	bfID_0.save()
	bmID_301,bmID_b_301 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hilbert-curve/')
	bmID_301.btitle='Hilbert Curve'
	bmID_301.bdescr='Hilbert Curve'
	bmID_301.save()
	bfID_301 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_301,bfrank=0.368476730931,clicks=67)
	bfID_301.save()
	bmID_160,bmID_b_160 = Bookmark.objects.get_or_create(url='http://exposedata.com/hypercube/rotate/')
	bmID_160.btitle='Rotating hypercube in orthogonal projection and parallel coordinates'
	bmID_160.bdescr='Rotating hypercube in orthogonal projection and parallel coordinates'
	bmID_160.save()
	bfID_160 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_160,bfrank=0.881312825934,clicks=43)
	bfID_160.save()
	bmID_211,bmID_b_211 = Bookmark.objects.get_or_create(url='http://www.dotuscomus.com/pergola/pergola_1.4.0/ExamplesHTML/D3/multiD3.html')
	bmID_211.btitle='D3 graphics in a Pergola SVG UI'
	bmID_211.bdescr='D3 graphics in a Pergola SVG UI'
	bmID_211.save()
	bfID_211 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_211,bfrank=0.944748243433,clicks=8)
	bfID_211.save()
	bmID_82,bmID_b_82 = Bookmark.objects.get_or_create(url='http://blog.pixelingene.com/2011/07/building-a-tree-diagram-in-d3-js/')
	bmID_82.btitle='Building a tree diagram'
	bmID_82.bdescr='Building a tree diagram'
	bmID_82.save()
	bfID_82 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_82,bfrank=0.889386319642,clicks=48)
	bfID_82.save()
	bmID_283,bmID_b_283 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/wordcloud/#http%3A%2F%2Fsearch.twitter.com%2Fsearch.json%3Frpp%3D100%26q%3D%7Bword%7D=cloud')
	bmID_283.btitle='Tag Cloud'
	bmID_283.bdescr='Tag Cloud'
	bmID_283.save()
	bfID_283 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_283,bfrank=0.172058569729,clicks=18)
	bfID_283.save()
	bmID_77,bmID_b_77 = Bookmark.objects.get_or_create(url='http://fanfarefantastique.com/vishna/')
	bmID_77.btitle='Hacker News Visualisation'
	bmID_77.bdescr='Hacker News Visualisation'
	bmID_77.save()
	bfID_77 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_77,bfrank=0.278636243633,clicks=25)
	bfID_77.save()
	bmID_326,bmID_b_326 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/movie')
	bmID_326.btitle='We re In The Money  How Much Do The Movies We Love Make '
	bmID_326.bdescr='We re In The Money  How Much Do The Movies We Love Make '
	bmID_326.save()
	bfID_326 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_326,bfrank=0.560966390484,clicks=4)
	bfID_326.save()
	bmID_92,bmID_b_92 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/building-cubic-hamiltonian-graphs-from-lcf-notation/')
	bmID_92.btitle='Building Cubic Hamiltonian Graphs from LCF Notation'
	bmID_92.bdescr='Building Cubic Hamiltonian Graphs from LCF Notation'
	bmID_92.save()
	bfID_92 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_92,bfrank=0.78738225816,clicks=40)
	bfID_92.save()
	bmID_222,bmID_b_222 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/parse/d3parse')
	bmID_222.btitle='d3 js partition chart serving data from parse com'
	bmID_222.bdescr='d3 js partition chart serving data from parse com'
	bmID_222.save()
	bfID_222 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_222,bfrank=0.601903360181,clicks=69)
	bfID_222.save()
	bmID_192,bmID_b_192 = Bookmark.objects.get_or_create(url='https://github.com/hhuuggoo/pushd3')
	bmID_192.btitle='Pushing d3 commands to the browser from iPython'
	bmID_192.bdescr='Pushing d3 commands to the browser from iPython'
	bmID_192.save()
	bfID_192 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_192,bfrank=0.804294971434,clicks=20)
	bfID_192.save()
	bmID_294,bmID_b_294 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/carotid/')
	bmID_294.btitle='Carotid Kundalini Fractal Explorer'
	bmID_294.bdescr='Carotid Kundalini Fractal Explorer'
	bmID_294.save()
	bfID_294 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_294,bfrank=0.710968008801,clicks=4)
	bfID_294.save()
	bmID_243,bmID_b_243 = Bookmark.objects.get_or_create(url='http://meshu.io/')
	bmID_243.btitle='Meshu turns your places into beautiful objects '
	bmID_243.bdescr='Meshu turns your places into beautiful objects '
	bmID_243.save()
	bfID_243 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_243,bfrank=0.554865020877,clicks=8)
	bfID_243.save()
	bmID_197,bmID_b_197 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/sankey')
	bmID_197.btitle='Sankey diagrams from Excel'
	bmID_197.bdescr='Sankey diagrams from Excel'
	bmID_197.save()
	bfID_197 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_197,bfrank=0.938067752597,clicks=23)
	bfID_197.save()
	bmID_170,bmID_b_170 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1367999')
	bmID_170.btitle='PJAX'
	bmID_170.bdescr='PJAX'
	bmID_170.save()
	bfID_170 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_170,bfrank=0.410246245955,clicks=88)
	bfID_170.save()
	bmID_98,bmID_b_98 = Bookmark.objects.get_or_create(url='http://jimkang.com/quadtreevis/')
	bmID_98.btitle='Interactive visualization that shows changes in the internal node tree of a quadtree as points are added'
	bmID_98.bdescr='Interactive visualization that shows changes in the internal node tree of a quadtree as points are added'
	bmID_98.save()
	bfID_98 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_98,bfrank=0.00536405036221,clicks=40)
	bfID_98.save()
	bmID_188,bmID_b_188 = Bookmark.objects.get_or_create(url='http://blogs.infoecho.net/echo/2012/02/05/ipython-notebook-d3-js-mashup/')
	bmID_188.btitle='IPython Notebook with d3 js'
	bmID_188.bdescr='IPython Notebook with d3 js'
	bmID_188.save()
	bfID_188 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_188,bfrank=0.958088928652,clicks=97)
	bfID_188.save()
	bmID_252,bmID_b_252 = Bookmark.objects.get_or_create(url='http://dimplejs.org/')
	bmID_252.btitle='Dimple'
	bmID_252.bdescr='Dimple'
	bmID_252.save()
	bfID_252 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_252,bfrank=0.637426367337,clicks=100)
	bfID_252.save()
	bmID_101,bmID_b_101 = Bookmark.objects.get_or_create(url='http://www.torre.nl/remittances/')
	bmID_101.btitle='Remittance flows'
	bmID_101.bdescr='Remittance flows'
	bmID_101.save()
	bfID_101 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_101,bfrank=0.341921968492,clicks=81)
	bfID_101.save()
	bmID_72,bmID_b_72 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1153292')
	bmID_72.btitle='Directed Edges  Curves and Arrow Markers '
	bmID_72.bdescr='Directed Edges  Curves and Arrow Markers '
	bmID_72.save()
	bfID_72 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_72,bfrank=0.59945179534,clicks=78)
	bfID_72.save()
	bmID_4,bmID_b_4 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/cod/')
	bmID_4.btitle='COD Visualization'
	bmID_4.bdescr='COD Visualization'
	bmID_4.save()
	bfID_4 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gozel,bfbookmark=bmID_4,bfrank=0.861261402212,clicks=4)
	bfID_4.save()
	bmID_250,bmID_b_250 = Bookmark.objects.get_or_create(url='http://nickqizhu.github.com/dc.js/')
	bmID_250.btitle='Dc js'
	bmID_250.bdescr='Dc js'
	bmID_250.save()
	bfID_250 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_250,bfrank=0.446638378509,clicks=36)
	bfID_250.save()
	bmID_93,bmID_b_93 = Bookmark.objects.get_or_create(url='http://thepowerrank.com/visual/NCAA_Tournament_Predictions')
	bmID_93.btitle='Circular tree  Will your team win the NCAA Tournament '
	bmID_93.bdescr='Circular tree  Will your team win the NCAA Tournament '
	bmID_93.save()
	bfID_93 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_93,bfrank=0.147430536059,clicks=86)
	bfID_93.save()
	bmID_159,bmID_b_159 = Bookmark.objects.get_or_create(url='http://latentflip.github.com/violin/')
	bmID_159.btitle='Violin  Instrumenting JavaScript'
	bmID_159.bdescr='Violin  Instrumenting JavaScript'
	bmID_159.save()
	bfID_159 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_159,bfrank=0.25048021739,clicks=90)
	bfID_159.save()
	bmID_15,bmID_b_15 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1134768')
	bmID_15.btitle='Stacked Bar Chart'
	bmID_15.bdescr='Stacked Bar Chart'
	bmID_15.save()
	bfID_15 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_15,bfrank=0.731380005327,clicks=12)
	bfID_15.save()
	bmID_14,bmID_b_14 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/882152')
	bmID_14.btitle='Grouped Bar Chart'
	bmID_14.bdescr='Grouped Bar Chart'
	bmID_14.save()
	bfID_14 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_14,bfrank=0.426801674431,clicks=79)
	bfID_14.save()
	bmID_135,bmID_b_135 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1073373')
	bmID_135.btitle='Force Directed States of America'
	bmID_135.bdescr='Force Directed States of America'
	bmID_135.save()
	bfID_135 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_135,bfrank=0.610300361388,clicks=93)
	bfID_135.save()
	bmID_61,bmID_b_61 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/kerryrodden/7090426')
	bmID_61.btitle='Using a sunburst to analyze sequences of events'
	bmID_61.bdescr='Using a sunburst to analyze sequences of events'
	bmID_61.save()
	bfID_61 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_61,bfrank=0.431380556657,clicks=16)
	bfID_61.save()
	bmID_287,bmID_b_287 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/graph-music/')
	bmID_287.btitle='The Music of Graphs'
	bmID_287.bdescr='The Music of Graphs'
	bmID_287.save()
	bfID_287 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_287,bfrank=0.813577511852,clicks=77)
	bfID_287.save()
	bmID_99,bmID_b_99 = Bookmark.objects.get_or_create(url='http://www.tips-for-excel.com/MCFC/Passes.html')
	bmID_99.btitle='Football passes'
	bmID_99.bdescr='Football passes'
	bmID_99.save()
	bfID_99 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_99,bfrank=0.416935335045,clicks=86)
	bfID_99.save()
	bmID_156,bmID_b_156 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3287802')
	bmID_156.btitle='Simple Dashboard Example'
	bmID_156.bdescr='Simple Dashboard Example'
	bmID_156.save()
	bfID_156 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_156,bfrank=0.306105967748,clicks=4)
	bfID_156.save()
	bmID_51,bmID_b_51 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1341281')
	bmID_51.btitle='Parallel Coordinates'
	bmID_51.bdescr='Parallel Coordinates'
	bmID_51.save()
	bfID_51 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_51,bfrank=0.426226808164,clicks=58)
	bfID_51.save()
	bmID_43,bmID_b_43 = Bookmark.objects.get_or_create(url='http://www.ericbullington.com/articles/2012/01/31/kmeans-visualization')
	bmID_43.btitle='Scatterplot for K Means clustering visualization'
	bmID_43.bdescr='Scatterplot for K Means clustering visualization'
	bmID_43.save()
	bfID_43 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_43,bfrank=0.0383720800625,clicks=70)
	bfID_43.save()
	bmID_183,bmID_b_183 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3173233')
	bmID_183.btitle='Loading Adobe Photoshop ASE color palette'
	bmID_183.bdescr='Loading Adobe Photoshop ASE color palette'
	bmID_183.save()
	bfID_183 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_183,bfrank=0.0576791265202,clicks=59)
	bfID_183.save()
	bmID_210,bmID_b_210 = Bookmark.objects.get_or_create(url='http://webmonarch.github.com/d34raphael/usage.html')
	bmID_210.btitle='d34raphael'
	bmID_210.bdescr='d34raphael'
	bmID_210.save()
	bfID_210 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_210,bfrank=0.166084278951,clicks=9)
	bfID_210.save()
	bmID_1,bmID_b_1 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/us-health-map')
	bmID_1.btitle='US Health Map'
	bmID_1.bdescr='US Health Map'
	bmID_1.save()
	bfID_1 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_1,bfrank=0.178393511179,clicks=85)
	bfID_1.save()
	bmID_299,bmID_b_299 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hamming-quilt/')
	bmID_299.btitle='Hamming Quilt'
	bmID_299.bdescr='Hamming Quilt'
	bmID_299.save()
	bfID_299 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_299,bfrank=0.447074268353,clicks=41)
	bfID_299.save()
	bmID_236,bmID_b_236 = Bookmark.objects.get_or_create(url='http://square.github.com/cube/')
	bmID_236.btitle='Cube  Time Series Data Collection  amp  Analysis'
	bmID_236.bdescr='Cube  Time Series Data Collection  amp  Analysis'
	bmID_236.save()
	bfID_236 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_236,bfrank=0.811862326614,clicks=30)
	bfID_236.save()
	bmID_50,bmID_b_50 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3921009')
	bmID_50.btitle='Sankey diagram with cycles'
	bmID_50.bdescr='Sankey diagram with cycles'
	bmID_50.save()
	bfID_50 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_50,bfrank=0.970013446336,clicks=67)
	bfID_50.save()
	bmID_162,bmID_b_162 = Bookmark.objects.get_or_create(url='http://metro.ezyang.com/')
	bmID_162.btitle='Metro Maps of the News'
	bmID_162.bdescr='Metro Maps of the News'
	bmID_162.save()
	bfID_162 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_162,bfrank=0.040565345556,clicks=69)
	bfID_162.save()
	bmID_206,bmID_b_206 = Bookmark.objects.get_or_create(url='http://exposedata.com/canvas/stacked.html')
	bmID_206.btitle='Canvas with d3 and Underscore'
	bmID_206.bdescr='Canvas with d3 and Underscore'
	bmID_206.save()
	bfID_206 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_206,bfrank=0.69030116161,clicks=89)
	bfID_206.save()
	bmID_144,bmID_b_144 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1276463')
	bmID_144.btitle='DOM to Canvas'
	bmID_144.bdescr='DOM to Canvas'
	bmID_144.save()
	bfID_144 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_144,bfrank=0.885569056683,clicks=30)
	bfID_144.save()
	bmID_90,bmID_b_90 = Bookmark.objects.get_or_create(url='http://maxdemarzi.com/2012/03/08/connections-in-time/')
	bmID_90.btitle='Connections in time'
	bmID_90.bdescr='Connections in time'
	bmID_90.save()
	bfID_90 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_90,bfrank=0.105870799123,clicks=84)
	bfID_90.save()
	bmID_314,bmID_b_314 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/morley-triangle/')
	bmID_314.btitle='Morley s trisector theorem'
	bmID_314.bdescr='Morley s trisector theorem'
	bmID_314.save()
	bfID_314 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_314,bfrank=0.116746248709,clicks=57)
	bfID_314.save()
	bmID_270,bmID_b_270 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/simplify/koch/')
	bmID_270.btitle='Quadratic Koch Island Simplification'
	bmID_270.bdescr='Quadratic Koch Island Simplification'
	bmID_270.save()
	bfID_270 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_270,bfrank=0.681276344951,clicks=74)
	bfID_270.save()
	bmID_233,bmID_b_233 = Bookmark.objects.get_or_create(url='http://www.ubiq.co')
	bmID_233.btitle='Ubiq Analytics  MySQL Analytics  amp  Reporting made easy'
	bmID_233.bdescr='Ubiq Analytics  MySQL Analytics  amp  Reporting made easy'
	bmID_233.save()
	bfID_233 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_233,bfrank=0.0696223663233,clicks=57)
	bfID_233.save()
	bmID_108,bmID_b_108 = Bookmark.objects.get_or_create(url='http://www.rjbaxley.com/p/publications.html')
	bmID_108.btitle='Co Authors Chords'
	bmID_108.bdescr='Co Authors Chords'
	bmID_108.save()
	bfID_108 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_108,bfrank=0.546142863874,clicks=90)
	bfID_108.save()
	bmID_322,bmID_b_322 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/gates/')
	bmID_322.btitle='Animated Bubble Chart of Gates Educational Donations'
	bmID_322.bdescr='Animated Bubble Chart of Gates Educational Donations'
	bmID_322.save()
	bfID_322 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_322,bfrank=0.649347053609,clicks=72)
	bfID_322.save()
	bmID_198,bmID_b_198 = Bookmark.objects.get_or_create(url='https://github.com/davidcox/plotsk')
	bmID_198.btitle='Plotsk  A python coffeescript d3 js based library for plotting data in a web browser'
	bmID_198.bdescr='Plotsk  A python coffeescript d3 js based library for plotting data in a web browser'
	bmID_198.save()
	bfID_198 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_198,bfrank=0.704844840231,clicks=5)
	bfID_198.save()
	bmID_132,bmID_b_132 = Bookmark.objects.get_or_create(url='http://ggruiz.me/weeknd3/')
	bmID_132.btitle='Weeknd3'
	bmID_132.bdescr='Weeknd3'
	bmID_132.save()
	bfID_132 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_132,bfrank=0.961940315453,clicks=62)
	bfID_132.save()
	bmID_140,bmID_b_140 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1256572')
	bmID_140.btitle='Show Reel'
	bmID_140.bdescr='Show Reel'
	bmID_140.save()
	bfID_140 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_140,bfrank=0.315628474994,clicks=88)
	bfID_140.save()
	bmID_28,bmID_b_28 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1157787')
	bmID_28.btitle='Small Multiples'
	bmID_28.bdescr='Small Multiples'
	bmID_28.save()
	bfID_28 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_28,bfrank=0.985662575837,clicks=37)
	bfID_28.save()
	bmID_29,bmID_b_29 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2011/08/08/simple-sparkline-using-svg-path-and-d3-js/')
	bmID_29.btitle='Sparklines'
	bmID_29.bdescr='Sparklines'
	bmID_29.save()
	bfID_29 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_29,bfrank=0.1545939011,clicks=97)
	bfID_29.save()
	bmID_26,bmID_b_26 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1624660')
	bmID_26.btitle='Variable width Histogram'
	bmID_26.bdescr='Variable width Histogram'
	bmID_26.save()
	bfID_26 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gozel,bfbookmark=bmID_26,bfrank=0.251550943613,clicks=27)
	bfID_26.save()
	bmID_208,bmID_b_208 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2294676')
	bmID_208.btitle='SVG to Canvas'
	bmID_208.bdescr='SVG to Canvas'
	bmID_208.save()
	bfID_208 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_208,bfrank=0.280943762521,clicks=31)
	bfID_208.save()
	bmID_256,bmID_b_256 = Bookmark.objects.get_or_create(url='https://github.com/vogievetsky/DVL')
	bmID_256.btitle='Dynamic Visualization LEGO'
	bmID_256.bdescr='Dynamic Visualization LEGO'
	bmID_256.save()
	bfID_256 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_256,bfrank=0.453983072178,clicks=68)
	bfID_256.save()
	bmID_185,bmID_b_185 = Bookmark.objects.get_or_create(url='http://ollieglass.com/2012/04/21/bieber-fever-meter-with-html5s-web-socket-d3-js-and-pusher/')
	bmID_185.btitle='Bieber Fever Meter with HTML5 s Web Socket  d3 js and Pusher'
	bmID_185.bdescr='Bieber Fever Meter with HTML5 s Web Socket  d3 js and Pusher'
	bmID_185.save()
	bfID_185 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_185,bfrank=0.266924317668,clicks=30)
	bfID_185.save()
	bmID_329,bmID_b_329 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/nationality_by_city.html')
	bmID_329.btitle='Proportion of Foreign Born in Large Cities  1900'
	bmID_329.bdescr='Proportion of Foreign Born in Large Cities  1900'
	bmID_329.save()
	bfID_329 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_329,bfrank=0.418577038062,clicks=97)
	bfID_329.save()
	bmID_102,bmID_b_102 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1046712')
	bmID_102.btitle='Dependencies Between Classes'
	bmID_102.bdescr='Dependencies Between Classes'
	bmID_102.save()
	bfID_102 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_102,bfrank=0.405546225152,clicks=72)
	bfID_102.save()
	bmID_129,bmID_b_129 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1016220')
	bmID_129.btitle='Line Tension'
	bmID_129.bdescr='Line Tension'
	bmID_129.save()
	bfID_129 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_129,bfrank=0.64829622203,clicks=49)
	bfID_129.save()
	bmID_47,bmID_b_47 = Bookmark.objects.get_or_create(url='http://benjiec.github.io/scatter-matrix/demo/demo.html')
	bmID_47.btitle='Explore Matrix Data with Scatterplots'
	bmID_47.bdescr='Explore Matrix Data with Scatterplots'
	bmID_47.save()
	bfID_47 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_47,bfrank=0.292743497771,clicks=31)
	bfID_47.save()
	bmID_316,bmID_b_316 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/pythagoras-proof/')
	bmID_316.btitle='Proof of Pythagoras  Theorem'
	bmID_316.bdescr='Proof of Pythagoras  Theorem'
	bmID_316.save()
	bfID_316 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_316,bfrank=0.863873185858,clicks=100)
	bfID_316.save()
	bmID_320,bmID_b_320 = Bookmark.objects.get_or_create(url='http://flowingdata.com/2012/08/02/how-to-make-an-interactive-network-visualization/')
	bmID_320.btitle='How to Make an Interactive Network Visualization'
	bmID_320.bdescr='How to Make an Interactive Network Visualization'
	bmID_320.save()
	bfID_320 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_320,bfrank=0.316653428671,clicks=8)
	bfID_320.save()
	bmID_31,bmID_b_31 = Bookmark.objects.get_or_create(url='http://mpf.vis.ywng.cloudbees.net/')
	bmID_31.btitle='Comprehensive Line Graph'
	bmID_31.bdescr='Comprehensive Line Graph'
	bmID_31.save()
	bfID_31 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_31,bfrank=0.918303540631,clicks=75)
	bfID_31.save()
	bmID_123,bmID_b_123 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3543186')
	bmID_123.btitle='Spiral for John Hunter'
	bmID_123.bdescr='Spiral for John Hunter'
	bmID_123.save()
	bfID_123 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_123,bfrank=0.36073219271,clicks=39)
	bfID_123.save()
	bmID_66,bmID_b_66 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/950642')
	bmID_66.btitle='Images and Labels'
	bmID_66.bdescr='Images and Labels'
	bmID_66.save()
	bfID_66 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_66,bfrank=0.0654751523397,clicks=63)
	bfID_66.save()
	bmID_240,bmID_b_240 = Bookmark.objects.get_or_create(url='http://chart.io/')
	bmID_240.btitle='Chart io  The Easiest Business Dashboard You ll Ever Use'
	bmID_240.bdescr='Chart io  The Easiest Business Dashboard You ll Ever Use'
	bmID_240.save()
	bfID_240 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_240,bfrank=0.825865826428,clicks=39)
	bfID_240.save()
	bmID_23,bmID_b_23 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1933560')
	bmID_23.btitle='Histogram Chart'
	bmID_23.bdescr='Histogram Chart'
	bmID_23.save()
	bfID_23 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gozel,bfbookmark=bmID_23,bfrank=0.460865180955,clicks=7)
	bfID_23.save()
	bmID_260,bmID_b_260 = Bookmark.objects.get_or_create(url='http://sepans.com/sp/postes/lepracursor/')
	bmID_260.btitle='Lepracursor'
	bmID_260.bdescr='Lepracursor'
	bmID_260.save()
	bfID_260 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_260,bfrank=0.76234925155,clicks=11)
	bfID_260.save()
	bmID_325,bmID_b_325 = Bookmark.objects.get_or_create(url='http://vallandingham.me/feltronifier/')
	bmID_325.btitle='Feltronifier'
	bmID_325.bdescr='Feltronifier'
	bmID_325.save()
	bfID_325 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_325,bfrank=0.11907724805,clicks=60)
	bfID_325.save()
	bmID_248,bmID_b_248 = Bookmark.objects.get_or_create(url='http://mortgagebloom.com')
	bmID_248.btitle='MortgageBloom Calculator'
	bmID_248.bdescr='MortgageBloom Calculator'
	bmID_248.save()
	bfID_248 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_248,bfrank=0.530178210184,clicks=30)
	bfID_248.save()
	bmID_215,bmID_b_215 = Bookmark.objects.get_or_create(url='http://maxdemarzi.com/2012/02/13/visualizing-a-network-with-cypher/')
	bmID_215.btitle='Visualizing a network with Cypher and d3 js'
	bmID_215.bdescr='Visualizing a network with Cypher and d3 js'
	bmID_215.save()
	bfID_215 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_215,bfrank=0.995360875157,clicks=46)
	bfID_215.save()
	bmID_262,bmID_b_262 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/nuitblanche.html')
	bmID_262.btitle='La Nuit Blanche'
	bmID_262.bdescr='La Nuit Blanche'
	bmID_262.save()
	bfID_262 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_262,bfrank=0.580019522065,clicks=99)
	bfID_262.save()
	bmID_214,bmID_b_214 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2759731')
	bmID_214.btitle='D3 heatmap using Backbone js and CoffeeScript'
	bmID_214.bdescr='D3 heatmap using Backbone js and CoffeeScript'
	bmID_214.save()
	bfID_214 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_214,bfrank=0.265703838242,clicks=72)
	bfID_214.save()
	bmID_20,bmID_b_20 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/rsloan/7123450')
	bmID_20.btitle='Waterfall Chart'
	bmID_20.bdescr='Waterfall Chart'
	bmID_20.save()
	bfID_20 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_20,bfrank=0.58616229525,clicks=44)
	bfID_20.save()
	bmID_297,bmID_b_297 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-quasicrystals/')
	bmID_297.btitle='Animated Quasicrystals'
	bmID_297.bdescr='Animated Quasicrystals'
	bmID_297.save()
	bfID_297 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_297,bfrank=0.645684108589,clicks=98)
	bfID_297.save()
	bmID_128,bmID_b_128 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062544')
	bmID_128.btitle='OMG Particles '
	bmID_128.bdescr='OMG Particles '
	bmID_128.save()
	bfID_128 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_128,bfrank=0.39542298166,clicks=85)
	bfID_128.save()
	bmID_35,bmID_b_35 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1314483')
	bmID_35.btitle='Stacked layout with time axis'
	bmID_35.bdescr='Stacked layout with time axis'
	bmID_35.save()
	bfID_35 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_35,bfrank=0.317914159479,clicks=60)
	bfID_35.save()
	bmID_226,bmID_b_226 = Bookmark.objects.get_or_create(url='http://www.d3-generator.com/')
	bmID_226.btitle='Bar chart code generator and online editor'
	bmID_226.bdescr='Bar chart code generator and online editor'
	bmID_226.save()
	bfID_226 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Jean,bfbookmark=bmID_226,bfrank=0.0309633121889,clicks=83)
	bfID_226.save()
	bmID_246,bmID_b_246 = Bookmark.objects.get_or_create(url='http://www.infocaptor.com')
	bmID_246.btitle='InfoCaptor Dashboards with D3 and canvas'
	bmID_246.bdescr='InfoCaptor Dashboards with D3 and canvas'
	bmID_246.save()
	bfID_246 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_246,bfrank=0.070362043432,clicks=72)
	bfID_246.save()
	bmID_207,bmID_b_207 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1846692')
	bmID_207.btitle='Automatically sizing text'
	bmID_207.bdescr='Automatically sizing text'
	bmID_207.save()
	bfID_207 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_207,bfrank=0.873287608763,clicks=67)
	bfID_207.save()
	bmID_169,bmID_b_169 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1503463')
	bmID_169.btitle='Masking with external svg elements'
	bmID_169.bdescr='Masking with external svg elements'
	bmID_169.save()
	bfID_169 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_169,bfrank=0.396104846973,clicks=95)
	bfID_169.save()
	bmID_107,bmID_b_107 = Bookmark.objects.get_or_create(url='http://fleetinbeing.net/d3e/chord.html')
	bmID_107.btitle='Chord Layout Transitions'
	bmID_107.bdescr='Chord Layout Transitions'
	bmID_107.save()
	bfID_107 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_107,bfrank=0.698407529006,clicks=3)
	bfID_107.save()
	bmID_168,bmID_b_168 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1071269')
	bmID_168.btitle='Date Ticks'
	bmID_168.bdescr='Date Ticks'
	bmID_168.save()
	bfID_168 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_168,bfrank=0.829376632218,clicks=67)
	bfID_168.save()
	bmID_217,bmID_b_217 = Bookmark.objects.get_or_create(url='http://briantford.com/blog/angular-d3.html')
	bmID_217.btitle='Using the D3 js Visualization Library with AngularJS'
	bmID_217.bdescr='Using the D3 js Visualization Library with AngularJS'
	bmID_217.save()
	bfID_217 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_217,bfrank=0.99048682193,clicks=18)
	bfID_217.save()
	bmID_267,bmID_b_267 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/polya.html')
	bmID_267.btitle='The Polya process'
	bmID_267.bdescr='The Polya process'
	bmID_267.save()
	bfID_267 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_267,bfrank=0.155044141363,clicks=94)
	bfID_267.save()
	bmID_245,bmID_b_245 = Bookmark.objects.get_or_create(url='http://nodal.me/login')
	bmID_245.btitle='Nodal is a fun way to view your GitHub network graph'
	bmID_245.bdescr='Nodal is a fun way to view your GitHub network graph'
	bmID_245.save()
	bfID_245 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_245,bfrank=0.514239691163,clicks=42)
	bfID_245.save()
	bmID_223,bmID_b_223 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/gassites/d3nodefocus')
	bmID_223.btitle='Force directed node focus generated from Excel'
	bmID_223.bdescr='Force directed node focus generated from Excel'
	bmID_223.save()
	bfID_223 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_223,bfrank=0.655033327089,clicks=85)
	bfID_223.save()
	bmID_75,bmID_b_75 = Bookmark.objects.get_or_create(url='http://www.torlaune.de/euro-2012/spieler-relationen/')
	bmID_75.btitle='Groups and Labels showing relations of football players participating in Euro 2012'
	bmID_75.bdescr='Groups and Labels showing relations of football players participating in Euro 2012'
	bmID_75.save()
	bfID_75 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_75,bfrank=0.197347648532,clicks=56)
	bfID_75.save()
	bmID_187,bmID_b_187 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4149176')
	bmID_187.btitle='Custom Multi Scale Time Format Axis'
	bmID_187.bdescr='Custom Multi Scale Time Format Axis'
	bmID_187.save()
	bfID_187 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_187,bfrank=0.909796255781,clicks=31)
	bfID_187.save()
	bmID_184,bmID_b_184 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4236639')
	bmID_184.btitle='Reusable text rotation'
	bmID_184.bdescr='Reusable text rotation'
	bmID_184.save()
	bfID_184 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_184,bfrank=0.692743746799,clicks=82)
	bfID_184.save()
	bmID_308,bmID_b_308 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-trig/')
	bmID_308.btitle='Animated Trigonometry'
	bmID_308.bdescr='Animated Trigonometry'
	bmID_308.save()
	bfID_308 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_308,bfrank=0.195615585378,clicks=15)
	bfID_308.save()
	bmID_271,bmID_b_271 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/random-points/')
	bmID_271.btitle='Random Points on a Sphere'
	bmID_271.bdescr='Random Points on a Sphere'
	bmID_271.save()
	bfID_271 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_271,bfrank=0.735650167962,clicks=2)
	bfID_271.save()
	bmID_209,bmID_b_209 = Bookmark.objects.get_or_create(url='https://github.com/mhemesath/r2d3/')
	bmID_209.btitle='d3 rendered with RaphaelJS for IE Compatibility'
	bmID_209.bdescr='d3 rendered with RaphaelJS for IE Compatibility'
	bmID_209.save()
	bfID_209 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_209,bfrank=0.595124713004,clicks=21)
	bfID_209.save()
	bmID_151,bmID_b_151 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1629464')
	bmID_151.btitle='Drag rectangle'
	bmID_151.bdescr='Drag rectangle'
	bmID_151.save()
	bfID_151 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_151,bfrank=0.525877419362,clicks=12)
	bfID_151.save()
	bmID_11,bmID_b_11 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/development-assistance-health-health-focus-area-global-1990-2009-interactiv')
	bmID_11.btitle='Development assistance for health by health focus area'
	bmID_11.bdescr='Development assistance for health by health focus area'
	bmID_11.save()
	bfID_11 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_11,bfrank=0.319058019764,clicks=94)
	bfID_11.save()
	bmID_146,bmID_b_146 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1386444')
	bmID_146.btitle='Square Circle Spiral Illusion'
	bmID_146.bdescr='Square Circle Spiral Illusion'
	bmID_146.save()
	bfID_146 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_146,bfrank=0.965259938074,clicks=12)
	bfID_146.save()
	bmID_230,bmID_b_230 = Bookmark.objects.get_or_create(url='http://phrogz.net/JS/d3-playground/#BlankDefault')
	bmID_230.btitle='D3 js playground'
	bmID_230.bdescr='D3 js playground'
	bmID_230.save()
	bfID_230 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_230,bfrank=0.896741564124,clicks=68)
	bfID_230.save()
	bmID_313,bmID_b_313 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/leibniz-spiral/')
	bmID_313.btitle='Leibniz Spiral'
	bmID_313.bdescr='Leibniz Spiral'
	bmID_313.save()
	bfID_313 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_313,bfrank=0.59676609638,clicks=23)
	bfID_313.save()
	bmID_244,bmID_b_244 = Bookmark.objects.get_or_create(url='http://www.simple.com/blog/Simple/announcing-reports')
	bmID_244.btitle='Reports for Simple'
	bmID_244.bdescr='Reports for Simple'
	bmID_244.save()
	bfID_244 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_244,bfrank=0.0756806475446,clicks=3)
	bfID_244.save()
	bmID_111,bmID_b_111 = Bookmark.objects.get_or_create(url='http://nbremer.blogspot.nl/2014/02/switching-behavior-between-phone-brands.html')
	bmID_111.btitle='Switching behavior between phone brands of the Dutch '
	bmID_111.bdescr='Switching behavior between phone brands of the Dutch '
	bmID_111.save()
	bfID_111 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_111,bfrank=0.1907109264,clicks=82)
	bfID_111.save()
	bmID_40,bmID_b_40 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1305111')
	bmID_40.btitle='Pie Multiples'
	bmID_40.bdescr='Pie Multiples'
	bmID_40.save()
	bfID_40 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gozel,bfbookmark=bmID_40,bfrank=0.561788268037,clicks=58)
	bfID_40.save()
	bmID_16,bmID_b_16 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1327441')
	bmID_16.btitle='Reorderable Stacked Bar Chart'
	bmID_16.bdescr='Reorderable Stacked Bar Chart'
	bmID_16.save()
	bfID_16 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_16,bfrank=0.577075337546,clicks=89)
	bfID_16.save()
	bmID_161,bmID_b_161 = Bookmark.objects.get_or_create(url='http://blog.lightjs.org/2012/10/welcome-to-webplatform-animation-d3js/')
	bmID_161.btitle='Webplatform dancing logo'
	bmID_161.bdescr='Webplatform dancing logo'
	bmID_161.save()
	bfID_161 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_161,bfrank=0.313072873511,clicks=28)
	bfID_161.save()
	bmID_191,bmID_b_191 = Bookmark.objects.get_or_create(url='http://www.drewconway.com/zia/?p=2765')
	bmID_191.btitle='Visualizing NetworkX graphs in the browser using D3'
	bmID_191.bdescr='Visualizing NetworkX graphs in the browser using D3'
	bmID_191.save()
	bfID_191 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_191,bfrank=0.0829789317878,clicks=65)
	bfID_191.save()
	bmID_255,bmID_b_255 = Bookmark.objects.get_or_create(url='https://github.com/shutterstock/rickshaw')
	bmID_255.btitle='Rickshaw  JavaScript toolkit for creating interactive real time graphs'
	bmID_255.bdescr='Rickshaw  JavaScript toolkit for creating interactive real time graphs'
	bmID_255.save()
	bfID_255 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_255,bfrank=0.700264386425,clicks=69)
	bfID_255.save()
	bmID_312,bmID_b_312 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/complete-graphs/')
	bmID_312.btitle='Complete Graphs'
	bmID_312.bdescr='Complete Graphs'
	bmID_312.save()
	bfID_312 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_312,bfrank=0.305872206776,clicks=53)
	bfID_312.save()
	bmID_175,bmID_b_175 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/shawnbot/BJLe6/')
	bmID_175.btitle='Responsive SVG resizing without re rendering'
	bmID_175.bdescr='Responsive SVG resizing without re rendering'
	bmID_175.save()
	bfID_175 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_175,bfrank=0.474382426512,clicks=92)
	bfID_175.save()
	bmID_321,bmID_b_321 = Bookmark.objects.get_or_create(url='http://vallandingham.me/bubble_cloud/')
	bmID_321.btitle='Word Frequency Bubble Clouds'
	bmID_321.bdescr='Word Frequency Bubble Clouds'
	bmID_321.save()
	bfID_321 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_321,bfrank=0.669705713887,clicks=43)
	bfID_321.save()
	bmID_285,bmID_b_285 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bml/')
	bmID_285.btitle='Biham Middleton Levine Traffic Model'
	bmID_285.bdescr='Biham Middleton Levine Traffic Model'
	bmID_285.save()
	bfID_285 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_285,bfrank=0.990560431665,clicks=38)
	bfID_285.save()
	bmID_65,bmID_b_65 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2920551')
	bmID_65.btitle='Multi Foci with Convex Hulls'
	bmID_65.bdescr='Multi Foci with Convex Hulls'
	bmID_65.save()
	bfID_65 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_65,bfrank=0.566997768446,clicks=78)
	bfID_65.save()
	bmID_68,bmID_b_68 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/929623')
	bmID_68.btitle='Interactive Construction'
	bmID_68.bdescr='Interactive Construction'
	bmID_68.save()
	bfID_68 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_68,bfrank=0.300220625511,clicks=82)
	bfID_68.save()
	bmID_304,bmID_b_304 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/earthquakes/#3.00/20.00/805.00')
	bmID_304.btitle='Latest Earthquakes'
	bmID_304.bdescr='Latest Earthquakes'
	bmID_304.save()
	bfID_304 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_304,bfrank=0.335246291339,clicks=29)
	bfID_304.save()
	bmID_25,bmID_b_25 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3048166')
	bmID_25.btitle='Fixed width Histogram of Durations  log normal distribution'
	bmID_25.bdescr='Fixed width Histogram of Durations  log normal distribution'
	bmID_25.save()
	bfID_25 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gozel,bfbookmark=bmID_25,bfrank=0.0339395612534,clicks=81)
	bfID_25.save()
	bmID_18,bmID_b_18 = Bookmark.objects.get_or_create(url='http://theoldbeggar.com/aid/')
	bmID_18.btitle='Sortable bars  Foreign aid  corruption and internet use'
	bmID_18.bdescr='Sortable bars  Foreign aid  corruption and internet use'
	bmID_18.save()
	bfID_18 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_18,bfrank=0.936070359412,clicks=4)
	bfID_18.save()
	bmID_265,bmID_b_265 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/ca.html')
	bmID_265.btitle='Cellular automata'
	bmID_265.bdescr='Cellular automata'
	bmID_265.save()
	bfID_265 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_265,bfrank=0.401811267081,clicks=42)
	bfID_265.save()
	bmID_114,bmID_b_114 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1067616')
	bmID_114.btitle='Venn Diagram using Opacity'
	bmID_114.bdescr='Venn Diagram using Opacity'
	bmID_114.save()
	bfID_114 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_114,bfrank=0.715461709214,clicks=52)
	bfID_114.save()
	bmID_117,bmID_b_117 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2011590')
	bmID_117.btitle='Chernoff faces'
	bmID_117.bdescr='Chernoff faces'
	bmID_117.save()
	bfID_117 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_117,bfrank=0.820565001455,clicks=34)
	bfID_117.save()
	bmID_37,bmID_b_37 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4175202')
	bmID_37.btitle='Multiple time series with object constancy'
	bmID_37.bdescr='Multiple time series with object constancy'
	bmID_37.save()
	bfID_37 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_37,bfrank=0.83567950289,clicks=9)
	bfID_37.save()
	bmID_80,bmID_b_80 = Bookmark.objects.get_or_create(url='http://disqus.com/gravity')
	bmID_80.btitle='Gravity by Disqus'
	bmID_80.bdescr='Gravity by Disqus'
	bmID_80.save()
	bfID_80 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_80,bfrank=0.636522914043,clicks=75)
	bfID_80.save()
	bmID_73,bmID_b_73 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1129492')
	bmID_73.btitle='Bounded Force Layout'
	bmID_73.bdescr='Bounded Force Layout'
	bmID_73.save()
	bfID_73 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_73,bfrank=0.300987685652,clicks=44)
	bfID_73.save()
	bmID_3,bmID_b_3 = Bookmark.objects.get_or_create(url='http://viz.healthmetricsandevaluation.org/mortality/')
	bmID_3.btitle='Mortality Visualization'
	bmID_3.bdescr='Mortality Visualization'
	bmID_3.save()
	bfID_3 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Gozel,bfbookmark=bmID_3,bfrank=0.218659641149,clicks=40)
	bfID_3.save()
	bmID_323,bmID_b_323 = Bookmark.objects.get_or_create(url='http://stowers.org/stowersreport/maps')
	bmID_323.btitle='Stowers Group Collaboration Network'
	bmID_323.bdescr='Stowers Group Collaboration Network'
	bmID_323.save()
	bfID_323 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_323,bfrank=0.731084748732,clicks=36)
	bfID_323.save()
	bmID_186,bmID_b_186 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4246925')
	bmID_186.btitle='Reverse Geocoding Plug in using an offline canvas'
	bmID_186.bdescr='Reverse Geocoding Plug in using an offline canvas'
	bmID_186.save()
	bfID_186 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_186,bfrank=0.876732113495,clicks=47)
	bfID_186.save()
	bmID_152,bmID_b_152 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1706523')
	bmID_152.btitle='Elastic collisions'
	bmID_152.bdescr='Elastic collisions'
	bmID_152.save()
	bfID_152 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_152,bfrank=0.763613515165,clicks=90)
	bfID_152.save()
	bmID_36,bmID_b_36 = Bookmark.objects.get_or_create(url='http://tympanus.net/codrops/2012/08/29/multiple-area-charts-with-d3-js/')
	bmID_36.btitle='Multiple Area Charts with D3 JS'
	bmID_36.bdescr='Multiple Area Charts with D3 JS'
	bmID_36.save()
	bfID_36 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_36,bfrank=0.115270551866,clicks=93)
	bfID_36.save()
	bmID_171,bmID_b_171 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1226718')
	bmID_171.btitle='Table Sorting'
	bmID_171.bdescr='Table Sorting'
	bmID_171.save()
	bfID_171 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_171,bfrank=0.479928955477,clicks=73)
	bfID_171.save()
	bmID_328,bmID_b_328 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/church_by_state.html')
	bmID_328.btitle='Composition of Church Membership by State  1890'
	bmID_328.bdescr='Composition of Church Membership by State  1890'
	bmID_328.save()
	bfID_328 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_328,bfrank=0.701330180834,clicks=6)
	bfID_328.save()
	bmID_224,bmID_b_224 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/flights')
	bmID_224.btitle='US Airline performance bigdata direct from Google Fusion'
	bmID_224.bdescr='US Airline performance bigdata direct from Google Fusion'
	bmID_224.save()
	bfID_224 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_224,bfrank=0.182818134283,clicks=56)
	bfID_224.save()
	bmID_10,bmID_b_10 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/life-expectancy-county-and-sex-us-country-comparison-global-1989-1999-2009')
	bmID_10.btitle='Life expectancy by county and sex  US  with country comparison'
	bmID_10.bdescr='Life expectancy by county and sex  US  with country comparison'
	bmID_10.save()
	bfID_10 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_10,bfrank=0.0677727935224,clicks=90)
	bfID_10.save()
	bmID_119,bmID_b_119 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2280295')
	bmID_119.btitle='Pictograms'
	bmID_119.bdescr='Pictograms'
	bmID_119.save()
	bfID_119 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_119,bfrank=0.0835367424138,clicks=25)
	bfID_119.save()
	bmID_309,bmID_b_309 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/apollonian-gasket/')
	bmID_309.btitle='Apollonian Gasket'
	bmID_309.bdescr='Apollonian Gasket'
	bmID_309.save()
	bfID_309 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_309,bfrank=0.256641458832,clicks=41)
	bfID_309.save()
	bmID_97,bmID_b_97 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4092944')
	bmID_97.btitle='Circular tree comparing the src directory for three versions of d3'
	bmID_97.bdescr='Circular tree comparing the src directory for three versions of d3'
	bmID_97.save()
	bfID_97 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_97,bfrank=0.785514925436,clicks=24)
	bfID_97.save()
	bmID_272,bmID_b_272 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/simplify/')
	bmID_272.btitle='Topology Preserving Geometry Simplification'
	bmID_272.bdescr='Topology Preserving Geometry Simplification'
	bmID_272.save()
	bfID_272 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_272,bfrank=0.840209921063,clicks=98)
	bfID_272.save()
	bmID_274,bmID_b_274 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/factorisation-diagrams/')
	bmID_274.btitle='Factorisation Diagrams'
	bmID_274.bdescr='Factorisation Diagrams'
	bmID_274.save()
	bfID_274 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_274,bfrank=0.314367487721,clicks=73)
	bfID_274.save()
	bmID_120,bmID_b_120 = Bookmark.objects.get_or_create(url='http://dyninc.github.com/d3-smokechart/')
	bmID_120.btitle='Smoke charts'
	bmID_120.bdescr='Smoke charts'
	bmID_120.save()
	bfID_120 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_120,bfrank=0.2706884565,clicks=51)
	bfID_120.save()
	bmID_181,bmID_b_181 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4047002')
	bmID_181.btitle='Custom Path and Area Generator'
	bmID_181.bdescr='Custom Path and Area Generator'
	bmID_181.save()
	bfID_181 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_181,bfrank=0.288864523449,clicks=15)
	bfID_181.save()
	bmID_153,bmID_b_153 = Bookmark.objects.get_or_create(url='http://blog.latentflip.com/post/18195267992/d3-collider')
	bmID_153.btitle='Collider   a d3 js game'
	bmID_153.bdescr='Collider   a d3 js game'
	bmID_153.save()
	bfID_153 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_153,bfrank=0.861752608239,clicks=17)
	bfID_153.save()
	bmID_147,bmID_b_147 = Bookmark.objects.get_or_create(url='https://github.com/enjalot/adventures_in_d3')
	bmID_147.btitle='Adventures in D3'
	bmID_147.bdescr='Adventures in D3'
	bmID_147.save()
	bfID_147 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_147,bfrank=0.953169172365,clicks=63)
	bfID_147.save()
	bmID_173,bmID_b_173 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1343714')
	bmID_173.btitle='Bay Area earthquake responses by zip code  loading external file through Yahoo Pipes'
	bmID_173.bdescr='Bay Area earthquake responses by zip code  loading external file through Yahoo Pipes'
	bmID_173.save()
	bfID_173 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_173,bfrank=0.788802279049,clicks=14)
	bfID_173.save()
	bmID_154,bmID_b_154 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1552725')
	bmID_154.btitle='alpha shapes aka concave hulls'
	bmID_154.bdescr='alpha shapes aka concave hulls'
	bmID_154.save()
	bfID_154 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_154,bfrank=0.63867994536,clicks=74)
	bfID_154.save()
	bmID_121,bmID_b_121 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/d/3779574/')
	bmID_121.btitle='Sankey Diagram with Overlap'
	bmID_121.bdescr='Sankey Diagram with Overlap'
	bmID_121.save()
	bfID_121 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_121,bfrank=0.135880568135,clicks=71)
	bfID_121.save()
	bmID_302,bmID_b_302 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/gaussian-primes/')
	bmID_302.btitle='Gaussian Primes'
	bmID_302.bdescr='Gaussian Primes'
	bmID_302.save()
	bfID_302 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_302,bfrank=0.971731836168,clicks=31)
	bfID_302.save()
	bmID_12,bmID_b_12 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/tools/data-visualization/development-assistance-health-channel-assistance-global-1990-2011-interacti')
	bmID_12.btitle='Development assistance for health by channel of assistance'
	bmID_12.bdescr='Development assistance for health by channel of assistance'
	bmID_12.save()
	bfID_12 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_12,bfrank=0.427252949111,clicks=93)
	bfID_12.save()
	bmID_127,bmID_b_127 = Bookmark.objects.get_or_create(url='http://mohdaslam.com/lte-rrc-rlc-mac-visualization-using-bubble-pack-layout/')
	bmID_127.btitle='LTE Protocol visualization'
	bmID_127.bdescr='LTE Protocol visualization'
	bmID_127.save()
	bfID_127 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_127,bfrank=0.610480085743,clicks=64)
	bfID_127.save()
	bmID_257,bmID_b_257 = Bookmark.objects.get_or_create(url='http://tenxer.github.com/xcharts/')
	bmID_257.btitle='xCharts  a D3 based library for building custom charts and graphs'
	bmID_257.bdescr='xCharts  a D3 based library for building custom charts and graphs'
	bmID_257.save()
	bfID_257 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_257,bfrank=0.785218578602,clicks=18)
	bfID_257.save()
	bmID_39,bmID_b_39 = Bookmark.objects.get_or_create(url='https://github.com/gajus/pie-chart')
	bmID_39.btitle='Reusable Pie Charts'
	bmID_39.bdescr='Reusable Pie Charts'
	bmID_39.save()
	bfID_39 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gozel,bfbookmark=bmID_39,bfrank=0.926218493349,clicks=3)
	bfID_39.save()
	bmID_78,bmID_b_78 = Bookmark.objects.get_or_create(url='http://pmsangal.tumblr.com/post/65499782255/visualizing-web-performance-1')
	bmID_78.btitle='Web performance'
	bmID_78.bdescr='Web performance'
	bmID_78.save()
	bfID_78 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_78,bfrank=0.565986911098,clicks=63)
	bfID_78.save()
	bmID_84,bmID_b_84 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/murray_3/5q62y/8/')
	bmID_84.btitle='Collpase expand nodes of a tree'
	bmID_84.bdescr='Collpase expand nodes of a tree'
	bmID_84.save()
	bfID_84 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_84,bfrank=0.0536067162242,clicks=99)
	bfID_84.save()
	bmID_86,bmID_b_86 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/999346')
	bmID_86.btitle='Animated'
	bmID_86.bdescr='Animated'
	bmID_86.save()
	bfID_86 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_86,bfrank=0.0712684180356,clicks=47)
	bfID_86.save()
	bmID_311,bmID_b_311 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/sorting/')
	bmID_311.btitle='Sorting Visualisations'
	bmID_311.bdescr='Sorting Visualisations'
	bmID_311.save()
	bfID_311 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_311,bfrank=0.973431473929,clicks=59)
	bfID_311.save()
	bmID_148,bmID_b_148 = Bookmark.objects.get_or_create(url='https://github.com/boorad/d3-tsline')
	bmID_148.btitle='Time Series'
	bmID_148.bdescr='Time Series'
	bmID_148.save()
	bfID_148 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_148,bfrank=0.601412879368,clicks=38)
	bfID_148.save()
	bmID_64,bmID_b_64 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021953')
	bmID_64.btitle='Multiple Foci'
	bmID_64.bdescr='Multiple Foci'
	bmID_64.save()
	bfID_64 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_64,bfrank=0.906171928422,clicks=41)
	bfID_64.save()
	bmID_237,bmID_b_237 = Bookmark.objects.get_or_create(url='http://square.github.com/tesseract/')
	bmID_237.btitle='Fast Multidimensional Filtering for Coordinated Views'
	bmID_237.bdescr='Fast Multidimensional Filtering for Coordinated Views'
	bmID_237.save()
	bfID_237 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_237,bfrank=0.407405604103,clicks=96)
	bfID_237.save()
	bmID_9,bmID_b_9 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-2010-healthy-years-lost-vs-life-expectancy')
	bmID_9.btitle='GBD 2010 healthy years lost vs life expectancy'
	bmID_9.bdescr='GBD 2010 healthy years lost vs life expectancy'
	bmID_9.save()
	bfID_9 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_9,bfrank=0.764169390857,clicks=68)
	bfID_9.save()
	bmID_165,bmID_b_165 = Bookmark.objects.get_or_create(url='http://jklabz.com/d3/digital_clock/digital_clock.html')
	bmID_165.btitle='Digital Clock By Virtual Force'
	bmID_165.bdescr='Digital Clock By Virtual Force'
	bmID_165.save()
	bfID_165 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_165,bfrank=0.251570851177,clicks=48)
	bfID_165.save()
	bmID_310,bmID_b_310 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bifurcation/')
	bmID_310.btitle='Monte Carlo simulation of bifurcations in the logistic map'
	bmID_310.bdescr='Monte Carlo simulation of bifurcations in the logistic map'
	bmID_310.save()
	bfID_310 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_310,bfrank=0.443783151985,clicks=75)
	bfID_310.save()
	bmID_216,bmID_b_216 = Bookmark.objects.get_or_create(url='https://github.com/hadley/r2d3')
	bmID_216.btitle='ggplot2   d3   r2d3'
	bmID_216.bdescr='ggplot2   d3   r2d3'
	bmID_216.save()
	bfID_216 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_216,bfrank=0.41400459218,clicks=47)
	bfID_216.save()
	bmID_234,bmID_b_234 = Bookmark.objects.get_or_create(url='https://www.droptask.com')
	bmID_234.btitle='DropTask  Visual task management application using D3 for visuals'
	bmID_234.bdescr='DropTask  Visual task management application using D3 for visuals'
	bmID_234.save()
	bfID_234 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_234,bfrank=0.566310633062,clicks=78)
	bfID_234.save()
	bmID_22,bmID_b_22 = Bookmark.objects.get_or_create(url='https://github.com/gajus/interdependent-interactive-histograms')
	bmID_22.btitle='Reusable Interdependent Interactive Histograms'
	bmID_22.bdescr='Reusable Interdependent Interactive Histograms'
	bmID_22.save()
	bfID_22 = BookmarkToFolder.objects.create(bffolder=f_Histogram_Gozel,bfbookmark=bmID_22,bfrank=0.363485052134,clicks=93)
	bfID_22.save()
	bmID_62,bmID_b_62 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062383')
	bmID_62.btitle='Symbols'
	bmID_62.bdescr='Symbols'
	bmID_62.save()
	bfID_62 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_62,bfrank=0.47751286559,clicks=51)
	bfID_62.save()
	bmID_124,bmID_b_124 = Bookmark.objects.get_or_create(url='http://nbremer.blogspot.com/2013/07/self-organizing-maps-adding-boundaries.html')
	bmID_124.btitle='Hexagonal Heatmaps for e g  Self Organizing Maps'
	bmID_124.bdescr='Hexagonal Heatmaps for e g  Self Organizing Maps'
	bmID_124.save()
	bfID_124 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_124,bfrank=0.789613346942,clicks=36)
	bfID_124.save()
	bmID_45,bmID_b_45 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/indiemaps/gzPDU/')
	bmID_45.btitle='Scatterplot and Heatmap'
	bmID_45.bdescr='Scatterplot and Heatmap'
	bmID_45.save()
	bfID_45 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_45,bfrank=0.412128993195,clicks=10)
	bfID_45.save()
	bmID_133,bmID_b_133 = Bookmark.objects.get_or_create(url='http://ggruiz.me/explosions/')
	bmID_133.btitle='Explosions'
	bmID_133.bdescr='Explosions'
	bmID_133.save()
	bfID_133 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_133,bfrank=0.539603885039,clicks=98)
	bfID_133.save()
	bmID_164,bmID_b_164 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4589092')
	bmID_164.btitle='Semi manual force layout of cablegate reference graphs'
	bmID_164.bdescr='Semi manual force layout of cablegate reference graphs'
	bmID_164.save()
	bfID_164 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_164,bfrank=0.82626794358,clicks=85)
	bfID_164.save()
	bmID_295,bmID_b_295 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/coffee-wheel/')
	bmID_295.btitle='Coffee Flavour Wheel'
	bmID_295.bdescr='Coffee Flavour Wheel'
	bmID_295.save()
	bfID_295 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_295,bfrank=0.411554692687,clicks=25)
	bfID_295.save()
	bmID_157,bmID_b_157 = Bookmark.objects.get_or_create(url='http://bollwyvl.github.com/blockd3/')
	bmID_157.btitle='Dataflow programming with D3 and Blockly'
	bmID_157.bdescr='Dataflow programming with D3 and Blockly'
	bmID_157.save()
	bfID_157 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_157,bfrank=0.443829730824,clicks=8)
	bfID_157.save()
	bmID_138,bmID_b_138 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1182434')
	bmID_138.btitle='Spline  Zoom and Pan'
	bmID_138.bdescr='Spline  Zoom and Pan'
	bmID_138.save()
	bfID_138 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_138,bfrank=0.777226092822,clicks=88)
	bfID_138.save()
	bmID_241,bmID_b_241 = Bookmark.objects.get_or_create(url='http://trisul.org/')
	bmID_241.btitle='Trisul Network Analytic'
	bmID_241.bdescr='Trisul Network Analytic'
	bmID_241.save()
	bfID_241 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_241,bfrank=0.322790042866,clicks=31)
	bfID_241.save()
	bmID_13,bmID_b_13 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1283663')
	bmID_13.btitle='Hierarchical Bar Chart'
	bmID_13.bdescr='Hierarchical Bar Chart'
	bmID_13.save()
	bfID_13 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_13,bfrank=0.837776269619,clicks=31)
	bfID_13.save()
	bmID_275,bmID_b_275 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bubbles/')
	bmID_275.btitle='Bubbles'
	bmID_275.bdescr='Bubbles'
	bmID_275.save()
	bfID_275 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_275,bfrank=0.557132438085,clicks=39)
	bfID_275.save()
	bmID_268,bmID_b_268 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/segregate.html')
	bmID_268.btitle='Schelling s segregation model'
	bmID_268.bdescr='Schelling s segregation model'
	bmID_268.save()
	bfID_268 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_268,bfrank=0.764283796373,clicks=30)
	bfID_268.save()
	bmID_145,bmID_b_145 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1345853')
	bmID_145.btitle='Transform Transitions'
	bmID_145.bdescr='Transform Transitions'
	bmID_145.save()
	bfID_145 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_145,bfrank=0.816293468182,clicks=70)
	bfID_145.save()
	bmID_112,bmID_b_112 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2206590')
	bmID_112.btitle='Click to Zoom with Albers Projection'
	bmID_112.bdescr='Click to Zoom with Albers Projection'
	bmID_112.save()
	bfID_112 = BookmarkToFolder.objects.create(bffolder=f_Maps_Jean,bfbookmark=bmID_112,bfrank=0.438302087723,clicks=3)
	bfID_112.save()
	bmID_76,bmID_b_76 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/chicago-lobbyists-force-directed-graph-visualization/')
	bmID_76.btitle='Chicago Lobbyists'
	bmID_76.bdescr='Chicago Lobbyists'
	bmID_76.save()
	bfID_76 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_76,bfrank=0.713923882907,clicks=93)
	bfID_76.save()
	bmID_300,bmID_b_300 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/hilbert-stocks/#GOOG,AAPL,ADBE,NTFL,AMZN,INTC,ARMH,A')
	bmID_300.btitle='Hilbert Stocks'
	bmID_300.bdescr='Hilbert Stocks'
	bmID_300.save()
	bfID_300 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_300,bfrank=0.691091280952,clicks=15)
	bfID_300.save()
	bmID_293,bmID_b_293 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/bloomfilter/')
	bmID_293.btitle='Bloom Filters'
	bmID_293.bdescr='Bloom Filters'
	bmID_293.save()
	bfID_293 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_293,bfrank=0.926228301739,clicks=14)
	bfID_293.save()
	bmID_91,bmID_b_91 = Bookmark.objects.get_or_create(url='http://www.christophermanning.org/projects/voronoi-diagram-with-force-directed-nodes-and-delaunay-links/')
	bmID_91.btitle='Voronoi Diagram with Force Directed Nodes and Delaunay Links'
	bmID_91.bdescr='Voronoi Diagram with Force Directed Nodes and Delaunay Links'
	bmID_91.save()
	bfID_91 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_91,bfrank=0.21884659049,clicks=62)
	bfID_91.save()
	bmID_327,bmID_b_327 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/racial_divide.html')
	bmID_327.btitle='Visualizing The Racial Divide'
	bmID_327.bdescr='Visualizing The Racial Divide'
	bmID_327.save()
	bfID_327 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_327,bfrank=0.971970463802,clicks=66)
	bfID_327.save()
	bmID_85,bmID_b_85 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2966094')
	bmID_85.btitle='Pedigree Tree'
	bmID_85.bdescr='Pedigree Tree'
	bmID_85.save()
	bfID_85 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_85,bfrank=0.551920246649,clicks=86)
	bfID_85.save()
	bmID_5,bmID_b_5 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-heatmap')
	bmID_5.btitle='GBD Heatmap'
	bmID_5.bdescr='GBD Heatmap'
	bmID_5.save()
	bfID_5 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_5,bfrank=0.434226520263,clicks=83)
	bfID_5.save()
	bmID_81,bmID_b_81 = Bookmark.objects.get_or_create(url='http://xliberation.com/googlecharts/d3nodefocustagsite.html')
	bmID_81.btitle='Navigate site by tags focus'
	bmID_81.bdescr='Navigate site by tags focus'
	bmID_81.save()
	bfID_81 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_81,bfrank=0.0780520676797,clicks=92)
	bfID_81.save()
	bmID_179,bmID_b_179 = Bookmark.objects.get_or_create(url='http://d3export.cancan.cshl.edu/')
	bmID_179.btitle='Export to SVG PNG PDF server side using Perl'
	bmID_179.bdescr='Export to SVG PNG PDF server side using Perl'
	bmID_179.save()
	bfID_179 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_179,bfrank=0.732043459849,clicks=55)
	bfID_179.save()
	bmID_199,bmID_b_199 = Bookmark.objects.get_or_create(url='http://blog.nextgenetics.net/?e=7')
	bmID_199.btitle='Data visualization with D3 js and python'
	bmID_199.bdescr='Data visualization with D3 js and python'
	bmID_199.save()
	bfID_199 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_199,bfrank=0.888976489005,clicks=43)
	bfID_199.save()
	bmID_113,bmID_b_113 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1067636')
	bmID_113.btitle='Venn Diagram using Clipping'
	bmID_113.bdescr='Venn Diagram using Clipping'
	bmID_113.save()
	bfID_113 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_113,bfrank=0.957014520703,clicks=78)
	bfID_113.save()
	bmID_54,bmID_b_54 = Bookmark.objects.get_or_create(url='http://www.theage.com.au/national/parsets')
	bmID_54.btitle='Parallel Sets with reorderable heading'
	bmID_54.bdescr='Parallel Sets with reorderable heading'
	bmID_54.save()
	bfID_54 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_54,bfrank=0.813274342637,clicks=68)
	bfID_54.save()
	bmID_30,bmID_b_30 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2012/05/15/interactive-line-graph-using-d3-js/')
	bmID_30.btitle='Interactive Line Graph'
	bmID_30.bdescr='Interactive Line Graph'
	bmID_30.save()
	bfID_30 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_30,bfrank=0.490443916853,clicks=99)
	bfID_30.save()
	bmID_83,bmID_b_83 = Bookmark.objects.get_or_create(url='http://blog.pixelingene.com/2011/08/progressive-reveal-animations-in-svg-using-a-svgclippath/')
	bmID_83.btitle='Reveal animation on a tree with a clip path'
	bmID_83.bdescr='Reveal animation on a tree with a clip path'
	bmID_83.save()
	bfID_83 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_83,bfrank=0.473090917925,clicks=35)
	bfID_83.save()
	bmID_229,bmID_b_229 = Bookmark.objects.get_or_create(url='http://enjalot.com/tributary/2165875/sinwaves.js')
	bmID_229.btitle='Tributary'
	bmID_229.bdescr='Tributary'
	bmID_229.save()
	bfID_229 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_229,bfrank=0.543694935576,clicks=60)
	bfID_229.save()
	bmID_227,bmID_b_227 = Bookmark.objects.get_or_create(url='http://www.bangongyun.com/chart')
	bmID_227.btitle='D3 bar chart online editor Chinese'
	bmID_227.bdescr='D3 bar chart online editor Chinese'
	bmID_227.save()
	bfID_227 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Jean,bfbookmark=bmID_227,bfrank=0.141501934025,clicks=42)
	bfID_227.save()
	bmID_174,bmID_b_174 = Bookmark.objects.get_or_create(url='http://jsfiddle.net/7WQjr/')
	bmID_174.btitle='Simple HTML data tables'
	bmID_174.bdescr='Simple HTML data tables'
	bmID_174.save()
	bfID_174 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_174,bfrank=0.454055149935,clicks=78)
	bfID_174.save()
	bmID_141,bmID_b_141 = Bookmark.objects.get_or_create(url='http://vvvvjs.quasipartikel.at/')
	bmID_141.btitle='VVVV viewer'
	bmID_141.bdescr='VVVV viewer'
	bmID_141.save()
	bfID_141 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_141,bfrank=0.758183971189,clicks=75)
	bfID_141.save()
	bmID_74,bmID_b_74 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1377729')
	bmID_74.btitle='Force Based Label Placement'
	bmID_74.bdescr='Force Based Label Placement'
	bmID_74.save()
	bfID_74 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_74,bfrank=0.765557796883,clicks=57)
	bfID_74.save()
	bmID_34,bmID_b_34 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1629644')
	bmID_34.btitle='Line Chart with tooltips'
	bmID_34.bdescr='Line Chart with tooltips'
	bmID_34.save()
	bfID_34 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_34,bfrank=0.238866352875,clicks=90)
	bfID_34.save()
	bmID_100,bmID_b_100 = Bookmark.objects.get_or_create(url='http://www.nu.nl/files/datajournalistiek/ek/ek2012.htm#.UKJ5yuOe8ww')
	bmID_100.btitle='Selecties EK 2012'
	bmID_100.bdescr='Selecties EK 2012'
	bmID_100.save()
	bfID_100 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_100,bfrank=0.642463771749,clicks=9)
	bfID_100.save()
	bmID_137,bmID_b_137 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1136236')
	bmID_137.btitle='Spermatozoa'
	bmID_137.bdescr='Spermatozoa'
	bmID_137.save()
	bfID_137 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_137,bfrank=0.195705766344,clicks=13)
	bfID_137.save()
	bmID_118,bmID_b_118 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1962173')
	bmID_118.btitle='Swimlane Chart'
	bmID_118.bdescr='Swimlane Chart'
	bmID_118.save()
	bfID_118 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_118,bfrank=0.633806946202,clicks=29)
	bfID_118.save()
	bmID_125,bmID_b_125 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021103')
	bmID_125.btitle='Superformula Explorer'
	bmID_125.bdescr='Superformula Explorer'
	bmID_125.save()
	bfID_125 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_125,bfrank=0.686349630782,clicks=50)
	bfID_125.save()
	bmID_220,bmID_b_220 = Bookmark.objects.get_or_create(url='http://timelyportfolio.blogspot.com/2012/12/d3-shiny-and-r-reporting-performance.html')
	bmID_220.btitle='Web reporting with D3js and R using RStudio Shiny'
	bmID_220.bdescr='Web reporting with D3js and R using RStudio Shiny'
	bmID_220.save()
	bfID_220 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_220,bfrank=0.548420726365,clicks=40)
	bfID_220.save()
	bmID_67,bmID_b_67 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2883411')
	bmID_67.btitle='Drag and Drop Support to set nodes to fixed position when dropped'
	bmID_67.bdescr='Drag and Drop Support to set nodes to fixed position when dropped'
	bmID_67.save()
	bfID_67 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_67,bfrank=0.225495116697,clicks=40)
	bfID_67.save()
	bmID_280,bmID_b_280 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/crayola/')
	bmID_280.btitle='Crayola Colour Chronology'
	bmID_280.bdescr='Crayola Colour Chronology'
	bmID_280.save()
	bfID_280 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_280,bfrank=0.189488495128,clicks=16)
	bfID_280.save()
	bmID_71,bmID_b_71 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2846454')
	bmID_71.btitle='From Matrix Market format'
	bmID_71.bdescr='From Matrix Market format'
	bmID_71.save()
	bfID_71 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_71,bfrank=0.162325896899,clicks=38)
	bfID_71.save()
	bmID_324,bmID_b_324 = Bookmark.objects.get_or_create(url='http://www.capitolmarkets.com/gsa-leased-investment-opportunity/')
	bmID_324.btitle='GSA Leased Opportunity Dashboard'
	bmID_324.bdescr='GSA Leased Opportunity Dashboard'
	bmID_324.save()
	bfID_324 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_324,bfrank=0.396233626302,clicks=80)
	bfID_324.save()
	bmID_55,bmID_b_55 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4168921')
	bmID_55.btitle='Pair Contribution and Selection'
	bmID_55.bdescr='Pair Contribution and Selection'
	bmID_55.save()
	bfID_55 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_55,bfrank=0.668250309827,clicks=2)
	bfID_55.save()
	bmID_176,bmID_b_176 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1691430')
	bmID_176.btitle='Automatic floating labels using d3 force layout'
	bmID_176.bdescr='Automatic floating labels using d3 force layout'
	bmID_176.save()
	bfID_176 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_176,bfrank=0.596470327535,clicks=97)
	bfID_176.save()
	bmID_218,bmID_b_218 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/partition')
	bmID_218.btitle='Zoomable Partition Charts directly from Excel'
	bmID_218.bdescr='Zoomable Partition Charts directly from Excel'
	bmID_218.save()
	bfID_218 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_218,bfrank=0.51154954618,clicks=85)
	bfID_218.save()
	bmID_281,bmID_b_281 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/parallel-sets/')
	bmID_281.btitle='Parallel Sets'
	bmID_281.bdescr='Parallel Sets'
	bmID_281.save()
	bfID_281 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_281,bfrank=0.502004877612,clicks=33)
	bfID_281.save()
	bmID_180,bmID_b_180 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4053096')
	bmID_180.btitle='Constraint relaxation 1'
	bmID_180.bdescr='Constraint relaxation 1'
	bmID_180.save()
	bfID_180 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_180,bfrank=0.185549133557,clicks=21)
	bfID_180.save()
	bmID_319,bmID_b_319 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/american-forces-in-afghanistan-and-iraq/')
	bmID_319.btitle='American Forces in Afghanistan and Iraq'
	bmID_319.bdescr='American Forces in Afghanistan and Iraq'
	bmID_319.save()
	bfID_319 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_319,bfrank=0.673120032262,clicks=63)
	bfID_319.save()
	bmID_228,bmID_b_228 = Bookmark.objects.get_or_create(url='http://livecoding.gabrielflor.it')
	bmID_228.btitle='Live coding based on Bret Victor s Inventing on Principle talk'
	bmID_228.bdescr='Live coding based on Bret Victor s Inventing on Principle talk'
	bmID_228.save()
	bfID_228 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_228,bfrank=0.817660818139,clicks=58)
	bfID_228.save()
	bmID_273,bmID_b_273 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/duplicates/')
	bmID_273.btitle='Detecting Duplicates in O 1  Space and O n  Time'
	bmID_273.bdescr='Detecting Duplicates in O 1  Space and O n  Time'
	bmID_273.save()
	bfID_273 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_273,bfrank=0.00313154112903,clicks=76)
	bfID_273.save()
	bmID_142,bmID_b_142 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1243323')
	bmID_142.btitle='Merge Sort'
	bmID_142.bdescr='Merge Sort'
	bmID_142.save()
	bfID_142 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_142,bfrank=0.369322182646,clicks=74)
	bfID_142.save()
	bmID_317,bmID_b_317 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/random-polygon-ellipse/')
	bmID_317.btitle='From Random Polygon to Ellipse'
	bmID_317.bdescr='From Random Polygon to Ellipse'
	bmID_317.save()
	bfID_317 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_317,bfrank=0.92346291246,clicks=73)
	bfID_317.save()
	bmID_105,bmID_b_105 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4062006')
	bmID_105.btitle='Fade on Hover'
	bmID_105.bdescr='Fade on Hover'
	bmID_105.save()
	bfID_105 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_105,bfrank=0.388128813293,clicks=27)
	bfID_105.save()
	bmID_8,bmID_b_8 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-cause-patterns')
	bmID_8.btitle='GBD Cause Patterns'
	bmID_8.bdescr='GBD Cause Patterns'
	bmID_8.save()
	bfID_8 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_8,bfrank=0.158118799039,clicks=80)
	bfID_8.save()
	bmID_289,bmID_b_289 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/mobile-lawsuits/')
	bmID_289.btitle='Mobile Patent Lawsuits'
	bmID_289.bdescr='Mobile Patent Lawsuits'
	bmID_289.save()
	bfID_289 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_289,bfrank=0.20589986662,clicks=2)
	bfID_289.save()
	bmID_122,bmID_b_122 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1044242')
	bmID_122.btitle='Hierarchical Edge Bundling'
	bmID_122.bdescr='Hierarchical Edge Bundling'
	bmID_122.save()
	bfID_122 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_122,bfrank=0.0619741299334,clicks=20)
	bfID_122.save()
	bmID_201,bmID_b_201 = Bookmark.objects.get_or_create(url='http://blog.echen.me/2012/03/05/instant-interactive-visualization-with-d3-and-ggplot2/')
	bmID_201.btitle='Instant interactive visualization with d3   ggplot2'
	bmID_201.bdescr='Instant interactive visualization with d3   ggplot2'
	bmID_201.save()
	bfID_201 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_201,bfrank=0.494909544499,clicks=79)
	bfID_201.save()
	bmID_33,bmID_b_33 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1483226')
	bmID_33.btitle='Horizon Chart'
	bmID_33.bdescr='Horizon Chart'
	bmID_33.save()
	bfID_33 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_33,bfrank=0.462352671763,clicks=96)
	bfID_33.save()
	bmID_269,bmID_b_269 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/maps/antipodes/')
	bmID_269.btitle='Antipodes'
	bmID_269.bdescr='Antipodes'
	bmID_269.save()
	bfID_269 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_269,bfrank=0.371343966427,clicks=88)
	bfID_269.save()
	bmID_96,bmID_b_96 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/972398')
	bmID_96.btitle='Treemap Layout in SVG'
	bmID_96.bdescr='Treemap Layout in SVG'
	bmID_96.save()
	bfID_96 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_96,bfrank=0.656249793138,clicks=16)
	bfID_96.save()
	bmID_21,bmID_b_21 = Bookmark.objects.get_or_create(url='https://github.com/liufly/Dual-scale-D3-Bar-Chart')
	bmID_21.btitle='Dual scale Bar Chart'
	bmID_21.bdescr='Dual scale Bar Chart'
	bmID_21.save()
	bfID_21 = BookmarkToFolder.objects.create(bffolder=f_Bar_Chart_Gozel,bfbookmark=bmID_21,bfrank=0.509012773593,clicks=5)
	bfID_21.save()
	bmID_247,bmID_b_247 = Bookmark.objects.get_or_create(url='https://www.moh.io/')
	bmID_247.btitle='Mohiomap  A Visual Memory for Evernote'
	bmID_247.bdescr='Mohiomap  A Visual Memory for Evernote'
	bmID_247.save()
	bfID_247 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_247,bfrank=0.42419094479,clicks=16)
	bfID_247.save()
	bmID_7,bmID_b_7 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-uncertainty-visualization')
	bmID_7.btitle='GBD Uncertainty Visualization'
	bmID_7.bdescr='GBD Uncertainty Visualization'
	bmID_7.save()
	bfID_7 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_7,bfrank=0.950828883186,clicks=73)
	bfID_7.save()
	bmID_196,bmID_b_196 = Bookmark.objects.get_or_create(url='https://bitbucket.org/davidagraf/dartsplaytree/src')
	bmID_196.btitle='Splay Tree animation with dart  d3  and local storage'
	bmID_196.bdescr='Splay Tree animation with dart  d3  and local storage'
	bmID_196.save()
	bfID_196 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_196,bfrank=0.900960038989,clicks=11)
	bfID_196.save()
	bmID_254,bmID_b_254 = Bookmark.objects.get_or_create(url='http://square.github.com/crossfilter/')
	bmID_254.btitle='Crossfilter'
	bmID_254.bdescr='Crossfilter'
	bmID_254.save()
	bfID_254 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_254,bfrank=0.243361254377,clicks=59)
	bfID_254.save()
	bmID_49,bmID_b_49 = Bookmark.objects.get_or_create(url='http://nickrabinowitz.com/projects/d3/alluvial/alluvial-dynamic.html')
	bmID_49.btitle='Animated Sankey Diagram  alluvial '
	bmID_49.bdescr='Animated Sankey Diagram  alluvial '
	bmID_49.save()
	bfID_49 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_49,bfrank=0.546730735651,clicks=59)
	bfID_49.save()
	bmID_48,bmID_b_48 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/llb4ll/8709363')
	bmID_48.btitle='k Nearest Neighbor Search with Quadtree'
	bmID_48.bdescr='k Nearest Neighbor Search with Quadtree'
	bmID_48.save()
	bfID_48 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_48,bfrank=0.376535495989,clicks=96)
	bfID_48.save()
	bmID_103,bmID_b_103 = Bookmark.objects.get_or_create(url='http://bost.ocks.org/mike/uberdata/')
	bmID_103.btitle='Uber Rides by Neighborhood'
	bmID_103.bdescr='Uber Rides by Neighborhood'
	bmID_103.save()
	bfID_103 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_103,bfrank=0.871226199286,clicks=77)
	bfID_103.save()
	bmID_286,bmID_b_286 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/9patch/')
	bmID_286.btitle='9 Patch Quilt Generator'
	bmID_286.bdescr='9 Patch Quilt Generator'
	bmID_286.save()
	bfID_286 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_286,bfrank=0.830443645881,clicks=75)
	bfID_286.save()
	bmID_94,bmID_b_94 = Bookmark.objects.get_or_create(url='http://blockses.appspot.com/2503502')
	bmID_94.btitle='Bracket Layout'
	bmID_94.bdescr='Bracket Layout'
	bmID_94.save()
	bfID_94 = BookmarkToFolder.objects.create(bffolder=f_Misc_Trees_and_Graphs_Wen,bfbookmark=bmID_94,bfrank=0.88649179614,clicks=100)
	bfID_94.save()
	bmID_53,bmID_b_53 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/parallel-sets/')
	bmID_53.btitle='Parallel Sets'
	bmID_53.bdescr='Parallel Sets'
	bmID_53.save()
	bfID_53 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_53,bfrank=0.614774419878,clicks=56)
	bfID_53.save()
	bmID_89,bmID_b_89 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1093025')
	bmID_89.btitle='Indented Tree  Collapsible '
	bmID_89.bdescr='Indented Tree  Collapsible '
	bmID_89.save()
	bfID_89 = BookmarkToFolder.objects.create(bffolder=f_Tree_Wen,bfbookmark=bmID_89,bfrank=0.0450510186937,clicks=4)
	bfID_89.save()
	bmID_63,bmID_b_63 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1021841')
	bmID_63.btitle='Custom Forces'
	bmID_63.bdescr='Custom Forces'
	bmID_63.save()
	bfID_63 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_63,bfrank=0.805346255566,clicks=93)
	bfID_63.save()
	bmID_116,bmID_b_116 = Bookmark.objects.get_or_create(url='http://tomerdoron.blogspot.com/2011/12/google-style-gauges-using-d3js.html')
	bmID_116.btitle='Gauge'
	bmID_116.bdescr='Gauge'
	bmID_116.save()
	bfID_116 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_116,bfrank=0.378860971298,clicks=52)
	bfID_116.save()
	bmID_69,bmID_b_69 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1062288')
	bmID_69.btitle='Collapsible Hierarchy'
	bmID_69.bdescr='Collapsible Hierarchy'
	bmID_69.save()
	bfID_69 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_69,bfrank=0.256861794386,clicks=74)
	bfID_69.save()
	bmID_261,bmID_b_261 = Bookmark.objects.get_or_create(url='http://iop.io/iopctrl')
	bmID_261.btitle='iopctrl js  User interface controls and gauges'
	bmID_261.bdescr='iopctrl js  User interface controls and gauges'
	bmID_261.save()
	bfID_261 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_261,bfrank=0.0237569405782,clicks=56)
	bfID_261.save()
	bmID_193,bmID_b_193 = Bookmark.objects.get_or_create(url='http://quasipartikel.at/2012/04/25/dancing-with-data/')
	bmID_193.btitle='Dance js  D3 with Backbone and Data js'
	bmID_193.bdescr='Dance js  D3 with Backbone and Data js'
	bmID_193.save()
	bfID_193 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_193,bfrank=0.210337093985,clicks=56)
	bfID_193.save()
	bmID_232,bmID_b_232 = Bookmark.objects.get_or_create(url='http://cssdeck.com/labs/d3-repulsive')
	bmID_232.btitle='CSSdeck  Repulsion example'
	bmID_232.bdescr='CSSdeck  Repulsion example'
	bmID_232.save()
	bfID_232 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_232,bfrank=0.168254939271,clicks=40)
	bfID_232.save()
	bmID_238,bmID_b_238 = Bookmark.objects.get_or_create(url='http://polychart.com/')
	bmID_238.btitle='Polychart  A browser based platform for exploring data and creating charts'
	bmID_238.bdescr='Polychart  A browser based platform for exploring data and creating charts'
	bmID_238.save()
	bfID_238 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_238,bfrank=0.811077975565,clicks=33)
	bfID_238.save()
	bmID_136,bmID_b_136 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1123639')
	bmID_136.btitle='Rounded Rectangles'
	bmID_136.bdescr='Rounded Rectangles'
	bmID_136.save()
	bfID_136 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_136,bfrank=0.579528190466,clicks=64)
	bfID_136.save()
	bmID_172,bmID_b_172 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/2295155')
	bmID_172.btitle='Templating ala Mustache  with Chernoff faces example'
	bmID_172.bdescr='Templating ala Mustache  with Chernoff faces example'
	bmID_172.save()
	bfID_172 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_172,bfrank=0.473641813256,clicks=15)
	bfID_172.save()
	bmID_195,bmID_b_195 = Bookmark.objects.get_or_create(url='http://blog.ouseful.info/2012/05/11/viewing-openlearn-mindmaps-using-d3-js/')
	bmID_195.btitle='Viewing OpenLearn Mindmaps Using d3 js'
	bmID_195.bdescr='Viewing OpenLearn Mindmaps Using d3 js'
	bmID_195.save()
	bfID_195 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_195,bfrank=0.636949510702,clicks=38)
	bfID_195.save()
	bmID_204,bmID_b_204 = Bookmark.objects.get_or_create(url='https://github.com/asutherland/d3-threeD')
	bmID_204.btitle='Very limited  in progress attempt to hook d3 js up to three js'
	bmID_204.bdescr='Very limited  in progress attempt to hook d3 js up to three js'
	bmID_204.save()
	bfID_204 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_204,bfrank=0.64205693003,clicks=16)
	bfID_204.save()
	bmID_242,bmID_b_242 = Bookmark.objects.get_or_create(url='http://exploreanalytics.com/')
	bmID_242.btitle='Explore Analytics  cloud based data analytics and visualization'
	bmID_242.bdescr='Explore Analytics  cloud based data analytics and visualization'
	bmID_242.save()
	bfID_242 = BookmarkToFolder.objects.create(bffolder=f_Products_Martyna,bfbookmark=bmID_242,bfrank=0.93471992632,clicks=18)
	bfID_242.save()
	bmID_46,bmID_b_46 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/4481531')
	bmID_46.btitle='Scatterplot  Social trust vs ease of doing business'
	bmID_46.bdescr='Scatterplot  Social trust vs ease of doing business'
	bmID_46.save()
	bfID_46 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_46,bfrank=0.330447830213,clicks=10)
	bfID_46.save()
	bmID_143,bmID_b_143 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1353700')
	bmID_143.btitle='Epicyclic Gearing'
	bmID_143.bdescr='Epicyclic Gearing'
	bmID_143.save()
	bfID_143 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_143,bfrank=0.775299288933,clicks=46)
	bfID_143.save()
	bmID_41,bmID_b_41 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1346395')
	bmID_41.btitle='Pie Chart Updating  Part 1 '
	bmID_41.bdescr='Pie Chart Updating  Part 1 '
	bmID_41.save()
	bfID_41 = BookmarkToFolder.objects.create(bffolder=f_Pie_Chart_Gozel,bfbookmark=bmID_41,bfrank=0.528927860331,clicks=63)
	bfID_41.save()
	bmID_60,bmID_b_60 = Bookmark.objects.get_or_create(url='http://xliberation.com/parse/colortable/parsed3.html')
	bmID_60.btitle='Sunburst  Color schemer with parse com integration'
	bmID_60.bdescr='Sunburst  Color schemer with parse com integration'
	bmID_60.save()
	bfID_60 = BookmarkToFolder.objects.create(bffolder=f_Sunburst_and_Partition_layout_Wen,bfbookmark=bmID_60,bfrank=0.266387948105,clicks=94)
	bfID_60.save()
	bmID_115,bmID_b_115 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1005090')
	bmID_115.btitle='Marimekko Chart'
	bmID_115.bdescr='Marimekko Chart'
	bmID_115.save()
	bfID_115 = BookmarkToFolder.objects.create(bffolder=f_Misc_Charts_Jean,bfbookmark=bmID_115,bfrank=0.0147839812125,clicks=16)
	bfID_115.save()
	bmID_266,bmID_b_266 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/life.html')
	bmID_266.btitle='Game of life'
	bmID_266.bdescr='Game of life'
	bmID_266.save()
	bfID_266 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_266,bfrank=0.827210236274,clicks=65)
	bfID_266.save()
	bmID_307,bmID_b_307 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/animated-bezier/')
	bmID_307.btitle='Animated B zier Curves'
	bmID_307.bdescr='Animated B zier Curves'
	bmID_307.save()
	bfID_307 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_307,bfrank=0.178689445584,clicks=38)
	bfID_307.save()
	bmID_6,bmID_b_6 = Bookmark.objects.get_or_create(url='http://www.healthmetricsandevaluation.org/gbd/visualizations/gbd-arrow-diagram')
	bmID_6.btitle='GBD Arrow Diagram'
	bmID_6.bdescr='GBD Arrow Diagram'
	bmID_6.save()
	bfID_6 = BookmarkToFolder.objects.create(bffolder=f_Institute_for_Health_Metrics_and_Evaluation_Gozel,bfbookmark=bmID_6,bfrank=0.588698624453,clicks=51)
	bfID_6.save()
	bmID_167,bmID_b_167 = Bookmark.objects.get_or_create(url='http://gist.github.com/plandem/5683951')
	bmID_167.btitle='Correct zoom for layout'
	bmID_167.bdescr='Correct zoom for layout'
	bmID_167.save()
	bfID_167 = BookmarkToFolder.objects.create(bffolder=f_Useful_snippets_Jean,bfbookmark=bmID_167,bfrank=0.0793220708531,clicks=55)
	bfID_167.save()
	bmID_296,bmID_b_296 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/17x17/')
	bmID_296.btitle='Number of unique rectangle free 4 colourings for an nxm grid'
	bmID_296.bdescr='Number of unique rectangle free 4 colourings for an nxm grid'
	bmID_296.save()
	bfID_296 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_296,bfrank=0.792840474617,clicks=58)
	bfID_296.save()
	bmID_44,bmID_b_44 = Bookmark.objects.get_or_create(url='http://slodge.com/teach/')
	bmID_44.btitle='Animated bubble charts for school data analysis'
	bmID_44.bdescr='Animated bubble charts for school data analysis'
	bmID_44.save()
	bfID_44 = BookmarkToFolder.objects.create(bffolder=f_Scatterplot_and_Bubble_chart_Gozel,bfbookmark=bmID_44,bfrank=0.792692709756,clicks=95)
	bfID_44.save()
	bmID_106,bmID_b_106 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/1308257')
	bmID_106.btitle='Static'
	bmID_106.bdescr='Static'
	bmID_106.save()
	bfID_106 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_106,bfrank=0.916960617597,clicks=71)
	bfID_106.save()
	bmID_291,bmID_b_291 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/girko-circle/')
	bmID_291.btitle='Girko s Circular Law'
	bmID_291.bdescr='Girko s Circular Law'
	bmID_291.save()
	bfID_291 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_291,bfrank=0.386617560653,clicks=30)
	bfID_291.save()
	bmID_277,bmID_b_277 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/primos/')
	bmID_277.btitle='El Patr n de los N meros Primos'
	bmID_277.bdescr='El Patr n de los N meros Primos'
	bmID_277.save()
	bfID_277 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_277,bfrank=0.7256811948,clicks=57)
	bfID_277.save()
	bmID_32,bmID_b_32 = Bookmark.objects.get_or_create(url='http://benjchristensen.com/2012/05/02/line-graphs-using-d3-js/')
	bmID_32.btitle='Dual scale line chart'
	bmID_32.bdescr='Dual scale line chart'
	bmID_32.save()
	bfID_32 = BookmarkToFolder.objects.create(bffolder=f_Line_and_Area_Chart_Gozel,bfbookmark=bmID_32,bfrank=0.0860318114382,clicks=31)
	bfID_32.save()
	bmID_251,bmID_b_251 = Bookmark.objects.get_or_create(url='http://nvd3.org/')
	bmID_251.btitle='NVD3'
	bmID_251.bdescr='NVD3'
	bmID_251.save()
	bfID_251 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_251,bfrank=0.595506218215,clicks=11)
	bfID_251.save()
	bmID_303,bmID_b_303 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/wave/')
	bmID_303.btitle='Wave'
	bmID_303.bdescr='Wave'
	bmID_303.save()
	bfID_303 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_303,bfrank=0.198978769836,clicks=29)
	bfID_303.save()
	bmID_264,bmID_b_264 = Bookmark.objects.get_or_create(url='http://www.jeromecukier.net/projects/models/markov.html')
	bmID_264.btitle='Markov processes'
	bmID_264.bdescr='Markov processes'
	bmID_264.save()
	bfID_264 = BookmarkToFolder.objects.create(bffolder=f_Jerome_Cukier_Martyna,bfbookmark=bmID_264,bfrank=0.48473690218,clicks=61)
	bfID_264.save()
	bmID_134,bmID_b_134 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1086421')
	bmID_134.btitle='Linear Gradients'
	bmID_134.bdescr='Linear Gradients'
	bmID_134.save()
	bfID_134 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_134,bfrank=0.565136877139,clicks=53)
	bfID_134.save()
	bmID_110,bmID_b_110 = Bookmark.objects.get_or_create(url='http://redotheweb.com/DependencyWheel/')
	bmID_110.btitle='Visualizing Package Dependencies'
	bmID_110.bdescr='Visualizing Package Dependencies'
	bmID_110.save()
	bfID_110 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Jean,bfbookmark=bmID_110,bfrank=0.320448485306,clicks=85)
	bfID_110.save()
	bmID_139,bmID_b_139 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/1098617')
	bmID_139.btitle='Arc Tweens'
	bmID_139.bdescr='Arc Tweens'
	bmID_139.save()
	bfID_139 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_139,bfrank=0.722216708958,clicks=45)
	bfID_139.save()
	bmID_318,bmID_b_318 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/tuebingen/')
	bmID_318.btitle='T bingen'
	bmID_318.bdescr='T bingen'
	bmID_318.save()
	bfID_318 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_318,bfrank=0.845242293831,clicks=99)
	bfID_318.save()
	bmID_163,bmID_b_163 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/d/2361485/')
	bmID_163.btitle='Life expectancy  small multiples'
	bmID_163.bdescr='Life expectancy  small multiples'
	bmID_163.save()
	bfID_163 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_163,bfrank=0.0886577548056,clicks=15)
	bfID_163.save()
	bmID_56,bmID_b_56 = Bookmark.objects.get_or_create(url='http://charts.graphicbaseball.com/parallelbatting')
	bmID_56.btitle='Graphicbaseball  2012 Batters'
	bmID_56.bdescr='Graphicbaseball  2012 Batters'
	bmID_56.save()
	bfID_56 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Wen,bfbookmark=bmID_56,bfrank=0.0130175064359,clicks=33)
	bfID_56.save()
	bmID_189,bmID_b_189 = Bookmark.objects.get_or_create(url='https://github.com/mikedewar/d3py')
	bmID_189.btitle='Plotting library for python based on d3'
	bmID_189.bdescr='Plotting library for python based on d3'
	bmID_189.save()
	bfID_189 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_189,bfrank=0.324089087409,clicks=7)
	bfID_189.save()
	bmID_330,bmID_b_330 = Bookmark.objects.get_or_create(url='http://vallandingham.me/vis/jobs_by_state.html')
	bmID_330.btitle='http   vallandingham me vis jobs_by_state html'
	bmID_330.bdescr='http   vallandingham me vis jobs_by_state html'
	bmID_330.save()
	bfID_330 = BookmarkToFolder.objects.create(bffolder=f_Jim_Vallandingham_James,bfbookmark=bmID_330,bfrank=0.79634195954,clicks=67)
	bfID_330.save()
	bmID_200,bmID_b_200 = Bookmark.objects.get_or_create(url='http://ramblings.mcpher.com/Home/excelquirks/d3/anyforce')
	bmID_200.btitle='d3 js force diagrams straight from Excel'
	bmID_200.bdescr='d3 js force diagrams straight from Excel'
	bmID_200.save()
	bfID_200 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_200,bfrank=0.88355192119,clicks=7)
	bfID_200.save()
	bmID_221,bmID_b_221 = Bookmark.objects.get_or_create(url='http://dexvis.com')
	bmID_221.btitle='Dex the Data Explorer'
	bmID_221.bdescr='Dex the Data Explorer'
	bmID_221.save()
	bfID_221 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_221,bfrank=0.00227964609745,clicks=96)
	bfID_221.save()
	bmID_52,bmID_b_52 = Bookmark.objects.get_or_create(url='http://bl.ocks.org/mbostock/3290263')
	bmID_52.btitle='Parallel coordinates with fisheye distortion'
	bmID_52.bdescr='Parallel coordinates with fisheye distortion'
	bmID_52.save()
	bfID_52 = BookmarkToFolder.objects.create(bffolder=f_Parallel_Coordinates_Parallel_sets_and_Sankey_Gozel,bfbookmark=bmID_52,bfrank=0.378780785477,clicks=98)
	bfID_52.save()
	bmID_306,bmID_b_306 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/voroboids/')
	bmID_306.btitle='Voronoi Boids  Voroboids'
	bmID_306.bdescr='Voronoi Boids  Voroboids'
	bmID_306.save()
	bfID_306 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_306,bfrank=0.399884083953,clicks=52)
	bfID_306.save()
	bmID_79,bmID_b_79 = Bookmark.objects.get_or_create(url='http://fcc.github.io/calltraffic/traffic2011.html')
	bmID_79.btitle='2011 International Phone Traffic'
	bmID_79.bdescr='2011 International Phone Traffic'
	bmID_79.save()
	bfID_79 = BookmarkToFolder.objects.create(bffolder=f_Force_Layout_Wen,bfbookmark=bmID_79,bfrank=0.630787900652,clicks=73)
	bfID_79.save()
	bmID_279,bmID_b_279 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/random-arboretum/')
	bmID_279.btitle='Random Arboretum'
	bmID_279.bdescr='Random Arboretum'
	bmID_279.save()
	bfID_279 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_279,bfrank=0.437229001283,clicks=40)
	bfID_279.save()
	bmID_258,bmID_b_258 = Bookmark.objects.get_or_create(url='http://www.visualsedimentation.org/')
	bmID_258.btitle='VisualSedimentation js  visualizing streaming data  inspired by the process of physical sedimentation'
	bmID_258.bdescr='VisualSedimentation js  visualizing streaming data  inspired by the process of physical sedimentation'
	bmID_258.save()
	bfID_258 = BookmarkToFolder.objects.create(bffolder=f_Libraries_Martyna,bfbookmark=bmID_258,bfrank=0.00736689851991,clicks=73)
	bfID_258.save()
	bmID_104,bmID_b_104 = Bookmark.objects.get_or_create(url='http://exposedata.com/tutorial/chord/latest.html')
	bmID_104.btitle='Updating data'
	bmID_104.bdescr='Updating data'
	bmID_104.save()
	bfID_104 = BookmarkToFolder.objects.create(bffolder=f_Chord_Layout_Wen,bfbookmark=bmID_104,bfrank=0.372058929291,clicks=37)
	bfID_104.save()
	bmID_212,bmID_b_212 = Bookmark.objects.get_or_create(url='http://sammyd.github.com/blog/2012/09/16/visualising-conair-data-with-cubism-dot-js/')
	bmID_212.btitle='Visualising ConAir Data With Cubism js  Arduino  TempoDB  Sinatra '
	bmID_212.bdescr='Visualising ConAir Data With Cubism js  Arduino  TempoDB  Sinatra '
	bmID_212.save()
	bfID_212 = BookmarkToFolder.objects.create(bffolder=f_Interoperability_Jean,bfbookmark=bmID_212,bfrank=0.336650105089,clicks=11)
	bfID_212.save()
	bmID_158,bmID_b_158 = Bookmark.objects.get_or_create(url='http://dan.iel.fm/xkcd/')
	bmID_158.btitle='XKCD style plots'
	bmID_158.bdescr='XKCD style plots'
	bmID_158.save()
	bfID_158 = BookmarkToFolder.objects.create(bffolder=f_Miscellaneous_visualizations_Jean,bfbookmark=bmID_158,bfrank=0.583595508147,clicks=91)
	bfID_158.save()
	bmID_249,bmID_b_249 = Bookmark.objects.get_or_create(url='http://apps.microsoft.com/windows/en-us/app/presentation-next/57c55802-1bdd-48c9-bf8b-e9e3c24cf051')
	bmID_249.btitle='Presentation Next  A Windows 8 HTML5 SVG Presentation Builder'
	bmID_249.bdescr='Presentation Next  A Windows 8 HTML5 SVG Presentation Builder'
	bmID_249.save()
	bfID_249 = BookmarkToFolder.objects.create(bffolder=f_Store_Apps_Martyna,bfbookmark=bmID_249,bfrank=0.279333043918,clicks=3)
	bfID_249.save()
	bmID_282,bmID_b_282 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/rhodonea/')
	bmID_282.btitle='Rhodonea Curve'
	bmID_282.bdescr='Rhodonea Curve'
	bmID_282.save()
	bfID_282 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_282,bfrank=0.986970741645,clicks=41)
	bfID_282.save()
	bmID_276,bmID_b_276 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/set-partitions/')
	bmID_276.btitle='Set Partitions'
	bmID_276.bdescr='Set Partitions'
	bmID_276.save()
	bfID_276 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_Martyna,bfbookmark=bmID_276,bfrank=0.0557944273802,clicks=76)
	bfID_276.save()
	bmID_315,bmID_b_315 = Bookmark.objects.get_or_create(url='http://www.jasondavies.com/poincare-disc/')
	bmID_315.btitle='Poincar  Disc'
	bmID_315.bdescr='Poincar  Disc'
	bmID_315.save()
	bfID_315 = BookmarkToFolder.objects.create(bffolder=f_Jason_Davies_James,bfbookmark=bmID_315,bfrank=0.646688491206,clicks=71)
	bfID_315.save()
	bmID_231,bmID_b_231 = Bookmark.objects.get_or_create(url='http://fleetinbeing.net/beans/d3')
	bmID_231.btitle='A CoffeeScript console for d3 js visualization'
	bmID_231.bdescr='A CoffeeScript console for d3 js visualization'
	bmID_231.save()
	bfID_231 = BookmarkToFolder.objects.create(bffolder=f_Online_Editors_Martyna,bfbookmark=bmID_231,bfrank=0.223925857793,clicks=34)
	bfID_231.save()

	#Bin Folders
	binID_0 = add_binfolder(busername_fk=Martyna)
	binID_1 = add_binfolder(busername_fk=James)
	binID_2 = add_binfolder(busername_fk=Gozel)
	binID_3 = add_binfolder(busername_fk=Jean)
	binID_4 = add_binfolder(busername_fk=Wen)

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
