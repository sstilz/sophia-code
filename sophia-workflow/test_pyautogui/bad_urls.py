def bad_urls_list():
	urls = [
		'https://www.jstor.org/stable/24874508?seq=1',
		'https://science.sciencemag.org/content/352/6292/1392',
		# 'https://www.cs.unm.edu/~forrest/classes/cs365/readings/feldman-rock-scissors-paper.pdf',  # PDF
		'https://science.sciencemag.org/content/219/4581/185',
		'https://pubmed.ncbi.nlm.nih.gov/9547323/',
		'https://www.jstor.org/stable/2399893?origin=crossref&seq=1',
		'https://dx.doi.org/10.1016/j.anbehav.2009.11.035',
		'http://www.int-res.com/abstracts/meps/v318/p153-163/',
		'https://science.sciencemag.org/content/320/5878/931.abstract?sid=1fc18835-728e-445d-bf7a-7ae5560c59f2',
		'http://meetings.aps.org/Meeting/DFD10/Event/133712',
		'https://stke.sciencemag.org/content/1/17/pe17',
		# 'https://core.ac.uk/download/pdf/11755576.pdf',  # PDF
		'https://www.jstor.org/stable/23436271?seq=1',
		'https://www.jstor.org/stable/3706047?seq=1',
		# 'https://www.jstage.jst.go.jp/article/tropics/7/1+2/7_1+2_93/_pdf/-char/ja',  # PDF
		'https://science.sciencemag.org/content/308/5730/1934',
		'https://www.jstor.org/stable/3882752?seq=1',
		'https://www.jstor.org/stable/1442721?origin=crossref&seq=1',
		'https://science.sciencemag.org/content/334/6063/1720',
		# 'https://www.uregina.ca/science/biology/people/faculty-research/brigham-mark/files/Woods_and_Brigham_2004_LITC.pdf',  # PDF
		'https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.103.184501',
		'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2002JB002326',
		# 'https://airtable.com/tblEY0y2cQYzXu2J5/viwORV9j9tIcpzcop',  # bad link
		'https://royalsocietypublishing.org/doi/full/10.1098/rspb.2010.1739 ',
		'https://www.thefreelibrary.com/Thoroughbred+structures%3A+an+unusual+bone+configuration+in+horses...-a098954045',
		# no DOI
		# 'https://aem.asm.org/content/aem/54/7/1678.full.pdf',  # PDF
		'https://www.jstor.org/stable/2410663?origin=crossref',
		'https://jlimnol.it/index.php/jlimnol/article/view/jlimnol.2004.s1.16',
		'https://www.jstor.org/stable/2260070?origin=crossref&seq=1',
		'https://www.jstor.org/stable/176791?seq=1',
		# 'https://www.jstor.org/stable/1309104 seq=1#metadata_info_tab_contents',  # bad link
		'https://jeb.biologists.org/content/210/8/1378',
		'https://jeb.biologists.org/content/31/4/491',
		'https://jeb.biologists.org/content/38/3/659',
		'https://archive.org/stream/biologicalbullet185mari/#page/n19/mode/1up',
		'https://science.sciencemag.org/content/328/5979/704',
		'https://science.sciencemag.org/content/298/5592/389',
		'https://science.sciencemag.org/content/349/6245/298',
		'https://science.sciencemag.org/content/325/5946/1351',
		'https://jeb.biologists.org/content/214/12/2047',
		'https://science.sciencemag.org/content/290/5500/2231.1',
		# 'http://connection.ebscohost.com/c/articles/9008131036/antifreeze-bees',  # bad link
		'https://www.jstor.org/stable/1538612?seq=1',
		'https://jeb.biologists.org/content/211/16/2647',
		'https://science.sciencemag.org/content/331/6014/183',
		'https://science.sciencemag.org/content/330/6008/1231',
		'https://science.sciencemag.org/content/332/6033/1097',
		'https://www.researchgate.net/publication/273142268_A_new_study_on_the_structure_and_function_of_the_adhesive_organs_of_the_Old_World_sucker-footed_bat_Myzopoda_Myzopodidae_of_Madagascar',
		'https://science.sciencemag.org/content/333/6038/52',
		'https://jeb.biologists.org/content/213/8/1235',
		'https://web.a.ebscohost.com/abstract?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=15691705&asa=Y&AN=26368786&h=sL1ulPZP3aO%2f4YDENSfYt%2fIaBmLJHv4%2fJhUQ7%2fC1BIu5MrGTIMJwx9CYogqyl6tcH5atqKlRraSD4T5fdWSSwQ%3d%3d&crl=c&resultNs=AdminWebAuth&resultLocal=ErrCrlNotAuth&crlhashurl=login.aspx%3fdirect%3dtrue%26profile%3dehost%26scope%3dsite%26authtype%3dcrawler%26jrnl%3d15691705%26asa%3dY%26AN%3d26368786',
		'https://pubmed.ncbi.nlm.nih.gov/9914146/',
		'https://jeb.biologists.org/content/207/18/3131',
		'https://jeb.biologists.org/content/198/9/1829',
		'https://science.sciencemag.org/content/243/4898/1589',
		# 'https://www.cell.com/current-biology/pdf/S0960-9822(02)00806-0.pdf',  # PDF
		'https://science.sciencemag.org/content/311/5767/1559',
		# 'https://www.nature.com/articles/s41467-020-14547-y.pdf?origin=ppub',  # PDF
		'https://science.sciencemag.org/content/194/4263/436',
		'https://jeb.biologists.org/content/217/8/1263',
		# 'https://www.scribd.com/document/411820185/inter-plant-communication-through-mycorrhizal-networks-mediates-complex-adaptive-behaviour-in-plant-communities',  # bad link
		'https://jeb.biologists.org/content/213/17/2967',
		'https://jeb.biologists.org/content/210/13/2231',
		'https://pubmed.ncbi.nlm.nih.gov/9202450/',
		'https://agris.fao.org/agris-search/search.do?recordID=QI9600003',
		'https://jeb.biologists.org/content/213/7/1115',
		# 'https://www.researchgate.net/publication/285796504_Fog_collection_by_Namib_Desert_Beetles',  # PDF (mostly)
		'https://jeb.biologists.org/content/214/23/3960',
		'https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.048704',
		'https://europepmc.org/article/med/12736997',
		'https://www.jstor.org/stable/2388496?seq=1',
		'https://jeb.biologists.org/content/207/2/211',
		'https://jeb.biologists.org/content/212/17/2835',
		'https://ui.adsabs.harvard.edu/abs/2010AIPC.1284....5M/abstract',
		'https://science.sciencemag.org/content/299/5611/1404',
		'https://www.jstor.org/stable/2441335?seq=1',
		'https://jeb.biologists.org/content/217/12/2193',
		'https://jeb.biologists.org/content/207/26/4633',
		'https://jeb.biologists.org/content/213/20/3457',
		'https://science.sciencemag.org/content/316/5826/884',
		'http://www.int-res.com/abstracts/ame/v15/n2/p153-163/',
		# 'https://bioone.org/journals/the-auk/volume-124/issue-4/0004-8038(2007)124%5b1244%3aSPFAOS%5d2.0.CO%3b2/SMALL-PREY-PROFITABILITY--FIELD-ANALYSIS-OF-SHOREBIRDS-USE-OF/10.1642/0004-8038(2007)124[1244:SPFAOS]2.0.CO;2.short',  # bad link
		'https://iopscience.iop.org/article/10.1088/1367-2630/15/12/125022/meta#artAbst',
		'https://jeb.biologists.org/content/210/13/2253',
		# 'http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.220.8508&rep=rep1&type=pdf',  # PDF
		'https://science.sciencemag.org/content/201/4356/614',
		'https://jeb.biologists.org/content/214/10/1699',
		'https://science.sciencemag.org/content/328/5975/216',
		'https://jeb.biologists.org/content/215/7/1151',
		# 'https://csme.utah.edu/wp-content/uploads/2013/02/Forest_Canopies_Plant_Diversity_Encyclopedia_of_Biodiversity_20011.pdf',  # PDF; bad link
		'https://www.jstor.org/stable/27855549?seq=1',
		'https://science.sciencemag.org/content/329/5991/559',
		'https://jeb.biologists.org/content/221/24/jeb192492',
		'https://jeb.biologists.org/content/212/13/1990',
		# 'https://bioone.org/journals/wetlands/volume-22/issue-2/0277-5212(2002)022%5B0430%3AIOSOFO%5D2.0.CO%3B2/INFLUENCE-OF-SEASON-OF-FIRE-ON-FLOWERING-OF-WET-PRAIRIE/10.1672/0277-5212(2002)022[0430:IOSOFO]2.0.CO;2.short',  # bad url
		'https://www.jstor.org/stable/2388018?seq=1',
		'https://www.jstor.org/stable/2406628?seq=1#metadata_info_tab_contents',
		'https://www.semanticscholar.org/paper/Architecture-and-morphogenesis-in-the-mound-of-in-Turner/1234b2b3f58f0d655d88589af43359d3ddbe57d3',
		# no DOI, only CorpusID
		'https://pubmed.ncbi.nlm.nih.gov/1159370/',
		'https://science.sciencemag.org/content/294/5548/1948',
		'https://www.jstor.org/stable/2388599?seq=1',
		'https://jeb.biologists.org/content/206/6/1059',
		'https://science.sciencemag.org/content/326/5956/1120',
		'https://jeb.biologists.org/content/214/22/3850',
		'https://jeb.biologists.org/content/215/9/1502',
		'https://jeb.biologists.org/content/205/5/651',
		# 'https://repository.si.edu/bitstream/handle/10088/7475/da1.pdf',  # PDF
		'https://science.sciencemag.org/content/337/6098/1087',
		# 'https://www.crossref.org/iPage?doi=10.1049%2Fji-1.1945.0103',  # abstract is PDF
		'https://science.sciencemag.org/content/296/5567/525',
		'https://science.sciencemag.org/content/317/5844/1561?etoc=',
		'https://jeb.biologists.org/content/208/8/1469',
		'https://science.sciencemag.org/content/243/4887/85',
		'https://iopscience.iop.org/article/10.1088/1748-3182/5/3/035005',
		'https://www.pnas.org/content/107/5/2082',
		'https://jeb.biologists.org/content/214/6/915',
		'https://jeb.biologists.org/content/212/19/3184',
		'https://www.jstor.org/stable/2835178?seq=1',
		# 'http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.605.7037&rep=rep1&type=pdf',  # DOI in link; PDF
		'https://jeb.biologists.org/content/213/19/3364',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.76.017301',
		'https://pdfs.semanticscholar.org/5d77/d11b2682c5eab61bbee638975cb73c8b02cc.pdf',
		'https://orbit.dtu.dk/en/publications/chemical-mediation-of-bacterial-surface-colonisation-by-secondary',
		# 'http://www.academicjournals.org/app/webroot/article/article1380190619_Kaupp%20and%20Kaupp.pdf',  # PDF
		'https://jeb.biologists.org/content/208/18/3609.abstract',
		'https://jeb.biologists.org/content/208/16/3075',
		'https://www.researchgate.net/publication/239919503_Characteristics_and_Impacts_of_Annual_vs_Perennial_Systems',
		'https://jeb.biologists.org/content/213/10/1731',
		'https://science.sciencemag.org/content/322/5899/275',
		'https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.048703',
		'https://jeb.biologists.org/content/210/15/2593',
		'https://jeb.biologists.org/content/207/7/1127',
		# 'https://books.google.com/books?hl=en&lr=&id=srWdAWBHyp4C&oi=fnd&pg=PP7&dq=animal+friendships&ots=Z15bpY087X&sig=1h5zhI8oaSMoXiRfFVaQcsTcaK4#v=onepage&q=animal%20friendships&f=false',  # bad link?
		'https://iopscience.iop.org/article/10.1088/0022-3727/40/7/050/meta',
		'https://jeb.biologists.org/content/192/1/45',
		'https://science.sciencemag.org/content/289/5486/1902',
		'https://science.sciencemag.org/content/313/5784/233',
		'https://www.jstor.org/stable/1366197?seq=1#metadata_info_tab_contents',
		'https://jeb.biologists.org/content/202/23/3315',
		'https://jeb.biologists.org/content/194/1/263.short',
		'https://jeb.biologists.org/content/210/19/3319',
		'https://science.sciencemag.org/content/318/5852/904',
		'https://jeb.biologists.org/content/210/14/2548',
		'https://jeb.biologists.org/content/212/21/3448',
		'https://jeb.biologists.org/content/208/8/1435',
		'https://iopscience.iop.org/article/10.1088/1748-3182/2/4/S01',
		'https://jeb.biologists.org/content/216/23/4473',
		'https://europepmc.org/article/med/26058145',
		'https://jeb.biologists.org/content/55/2/385.article-info',
		'https://jeb.biologists.org/content/212/21/3499',
		'https://science.sciencemag.org/content/305/5682/402',
		'https://jeb.biologists.org/content/212/21/3440',
		'https://science.sciencemag.org/content/291/5510/1884',
		'https://science.sciencemag.org/content/292/5526/2495',
		'https://pubmed.ncbi.nlm.nih.gov/10441082/',
		'https://www.jstor.org/stable/1542085?seq=1',
		'https://www.jstor.org/stable/2388261?origin=crossref&seq=1',
		'https://jeb.biologists.org/content/213/2/249',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.74.051916',
		'https://jeb.biologists.org/content/69/1/127',
		'https://jeb.biologists.org/content/209/5/938',
		# 'http://umdberg.pbworks.com/w/file/fetch/47150934/wikelski%202002.pdf',  # PDF
		# 'https://www.nature.com/articles/176657a0.epdf',  # PDF
		'https://jeb.biologists.org/content/210/13/2300',
		'https://www.jstor.org/stable/2259780?origin=crossref&seq=1',
		'https://www.jstor.org/stable/23384962?seq=1#page_scan_tab_contents',
		'https://science.sciencemag.org/content/296/5566/250',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.82.011910',
		# 'https://www.nature.com/articles/247074a0.pdf?proof=true',  # PDF
		'https://jeb.biologists.org/content/213/15/2665',
		'https://doi.org/10.1016/j.scitotenv.2017.06.173',
		'http://www.int-res.com/abstracts/cr/v05/n1/p53-59/',
		'https://science.sciencemag.org/content/302/5650/1566',
		'https://jeb.biologists.org/content/206/23/4217',
		'http://dx.doi.org/10.1126/science.1188761',
		'https://onlinelibrary.wiley.com/doi/abs/10.1002/we.1804',
		'https://iopscience.iop.org/article/10.1088/1748-3182/2/3/L01',
		'https://jeb.biologists.org/content/210/15/2593.long',
		'https://jcs.biologists.org/content/114/6/1061.short',
		'https://www.researchgate.net/profile/Jason_Hoeksema/publication/46254430_Mycorrhizal_networks_counteract_competitive_effects_of_canopy_trees_on_seedling_survival/links/5a0a0c2645851551b78d2c85/Mycorrhizal-networks-counteract-competitive-effects-of-canopy-trees-on-seedling-survival.pdf',
		'https://jeb.biologists.org/content/193/1/233',
		'https://jeb.biologists.org/content/213/20/3416',
		'https://jeb.biologists.org/content/214/13/2175',
		'https://science.sciencemag.org/content/293/5527/102',
		'https://www.researchgate.net/publication/238671399_%27Eight-legged_cats%27_and_how_they_see_-_A_review_of_recent_research_on_jumping_spiders_Araneae_Salticidae',
		'https://pubmed.ncbi.nlm.nih.gov/9697323/',
		'https://jeb.biologists.org/content/218/22/3551',
		'https://jeb.biologists.org/content/152/1/243.short',
		# 'https://www.yumpu.com/en/document/read/40748212/toward-biomimetic-architecture-annapujadascat',  # bad link
		'https://jeb.biologists.org/content/215/12/2072',
		# 'https://jeb.biologists.org/content/jexbio/201/5/673.full.pdf',  # PDF
		'https://iopscience.iop.org/article/10.1088/0953-8984/17/9/021',
		'https://science.sciencemag.org/content/330/6005/816',
		'https://www.jstor.org/stable/3762235?seq=1',
		'https://jeb.biologists.org/content/214/17/2988',
		# 'https://kuscholarworks.ku.edu/bitstream/handle/1808/6134/Fautin.1991.pdf?sequence=1&isAllowed=y',  # PDF
		'https://jeb.biologists.org/content/21/3-4/97',
		'https://science.sciencemag.org/content/325/5939/468',
		'https://jeb.biologists.org/content/213/7/1092',
		'http://www.2008.botanyconference.org/engine/search/index.php?func=detail&aid=343',
		'https://jeb.biologists.org/content/163/1/1.short',
		'https://jeb.biologists.org/content/208/23/4467',
		# 'https://www.conservationgateway.org/ConservationPractices/Marine/crr/library/Documents/wind-and-swell-wave-reduction-by-mangroves.pdf',  # PDF
		'https://jeb.biologists.org/content/213/5/673',
		'https://science.sciencemag.org/content/316/5831/1600',
		'https://jeb.biologists.org/content/216/11/1961',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.94.032403',
		'https://www.jstor.org/stable/1565146?origin=crossref&seq=1',
		'https://www.ncbi.nlm.nih.gov/pubmed/11893768',
		'https://science.sciencemag.org/content/290/5497/1744',
		'https://pubmed.ncbi.nlm.nih.gov/9787125/',
		'https://jeb.biologists.org/content/202/23/3305',
		'https://www.jstor.org/stable/1447748?origin=crossref&seq=1',
		'http://www.int-res.com/abstracts/ame/v47/n3/p275-287/',
		'https://jeb.biologists.org/content/213/3/469',
		'https://www.jstor.org/stable/1565367?origin=crossref&seq=1',
		'https://linkinghub.elsevier.com/retrieve/pii/S0169534719302563',
		# 'https://spo.nmfs.noaa.gov/sites/default/files/pdf-content/1982/802/hain.pdf',  # PDF
		'https://science.sciencemag.org/content/289/5487/2114',
		'https://jeb.biologists.org/content/213/10/1697',
		'https://science.sciencemag.org/content/327/5966/701',
		'https://iopscience.iop.org/article/10.1088/0960-1317/15/7/011',
		'https://science.sciencemag.org/content/204/4391/415.long',
		'https://www.jstor.org/stable/1564398?origin=crossref&seq=1',
		'https://jeb.biologists.org/content/209/2/202',
		'https://jeb.biologists.org/content/206/20/3581',
		'https://www.semanticscholar.org/paper/Arsenic-hyperaccumulating-ferns-and-their-to-of-Rathinasabapathi-Ma/36f64296e760af7924d99b00bd9554cf1bfe94ad',
		'https://jeb.biologists.org/content/212/24/4002',
		'https://iopscience.iop.org/article/10.1088/1748-3182/6/4/046001',
		'https://jeb.biologists.org/content/214/5/848',
		'https://science.sciencemag.org/content/316/5827/1030',
		'https://jeb.biologists.org/content/208/8/1445',
		'https://jeb.biologists.org/content/135/1/431',
		'https://www.publish.csiro.au/mf/MF97051',
		'https://science.sciencemag.org/content/325/5943/964',
		'https://jeb.biologists.org/content/56/1/195.short',
		'https://jeb.biologists.org/content/159/1/419',
		# 'http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.386.8668&rep=rep1&type=pdf',  # PDF
		'https://jeb.biologists.org/content/203/18/2757',
		'https://pubmed.ncbi.nlm.nih.gov/945321/',
		'https://www.omicsonline.org/open-access/biological-activities-of-rice-allelochemicals-momilactone-a-and-b-jrr.1000108.php?aid=21069',
		'https://jeb.biologists.org/content/211/5/717',
		'https://www.jstor.org/stable/1310784',
		'http://www.int-res.com/abstracts/meps/v207/p227-241/',
		# 'https://drive.google.com/viewerng/viewer?url=https://www.fpl.fs.fed.us/documnts/fplgtr/fplgtr190/chapter_03.pdf',  # PDF
		'https://www.springer.com/gp/book/9780412561603',
		'https://science.sciencemag.org/content/193/4252/484',
		'https://www.jstor.org/stable/10.1086/678955?seq=1',
		'https://jeb.biologists.org/content/207/24/4249',
		'https://jeb.biologists.org/content/134/1/313',
		'https://jeb.biologists.org/content/211/21/3421',
		'https://pdfs.semanticscholar.org/4441/fe4a695da6b5a9d7b8aa5073b9f0e89768d5.pdf',
		'https://www.jstor.org/stable/2398919?seq=1',
		'https://jeb.biologists.org/content/215/4/578',
		'https://jeb.biologists.org/content/207/7/1063',
		# 'https://www.cell.com/biophysj/pdf/S0006-3495(71)86276-8.pdf',  # PDF
		# 'https://www.tandfonline.com/doi/pdf/10.1080/00445096.1973.11448511',  # PDF
		'https://science.sciencemag.org/content/317/5842/1189',
		'https://science.sciencemag.org/content/346/6206/224',
		'https://www.jstor.org/stable/4159449?seq=1',
		'https://jeb.biologists.org/content/209/4/748',
		'https://www.jstor.org/stable/1443948?origin=crossref&seq=1',
		'https://science.sciencemag.org/content/327/5966/689',
		'https://science.sciencemag.org/content/326/5950/289',
		'https://www.jstor.org/stable/1438539?seq=1',
		'https://ieeexplore.ieee.org/document/1225901',
		'https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.104.158302',
		'https://iopscience.iop.org/article/10.1088/1367-2630/10/3/033014',
		'https://science.sciencemag.org/content/311/5767/1580',
		# 'https://jeb.biologists.org/content/jexbio/203/23/3585.full.pdf',  # PDF
		'https://jeb.biologists.org/content/113/1/447.abstract',
		'https://jeb.biologists.org/content/215/23/4217',
		'https://jeb.biologists.org/content/212/13/1981',
		'https://jeb.biologists.org/content/212/24/4010',
		'https://www.ncbi.nlm.nih.gov/books/NBK10895/',
		'https://www.jstor.org/stable/2388261?seq=1',
		'https://science.sciencemag.org/content/318/5849/426',
		'https://jeb.biologists.org/content/69/1/127.abstract',
		'https://jeb.biologists.org/content/202/20/2727.long',
		'https://www.jstor.org/stable/1447745?origin=crossref&seq=1',
		'https://jeb.biologists.org/content/200/3/557',
		'https://science.sciencemag.org/content/349/6243/aaa6683',
		# 'https://books.google.com/books?id=ILFpAAAAMAAJ&lpg=PR11&ots=3pmzsRwISC&dq=Olfaction%20and%20Taste%3A%20Proceedings%20of%20the%20Third%20International%20Symposium&lr&pg=PR11#v=onepage&q=Olfaction%20and%20Taste:%20Proceedings%20of%20the%20Third%20International%20Symposium&f=false',  # bad link
		'https://science.sciencemag.org/content/334/6055/528.long',
		'https://iopscience.iop.org/article/10.1088/0957-4484/13/5/201',
		'https://www.jstor.org/stable/1446299?origin=crossref&seq=1',
		'https://science.sciencemag.org/content/202/4369/747',
		'https://jeb.biologists.org/content/214/4/521',
		'https://jeb.biologists.org/content/88/1/1',
		'https://www.jstor.org/stable/1565147?origin=crossref&seq=1',
		'https://jeb.biologists.org/content/212/3/429',
		# 'http://members.optusnet.com.au/elanbee/Den%20Speciosum%20%26%20Bushfire_PBAdams-SDLawson.pdf',  # PDF
		'https://ieeexplore.ieee.org/document/6608113',
		'https://link.springer.com/chapter/10.1007/b98314',
		'https://jeb.biologists.org/content/199/4/1005',
		'https://iopscience.iop.org/article/10.1088/1748-3182/5/3/035001',
		'https://science.sciencemag.org/content/319/5871/1816',
		'https://jeb.biologists.org/content/215/8/1247',
		'https://science.sciencemag.org/content/212/4501/1397',
		'https://science.sciencemag.org/content/325/5946/1388',
		'https://science.sciencemag.org/content/306/5701/1565',
		'https://jeb.biologists.org/content/201/11/1681.short',
		'http://drs.nio.org/drs/handle/2264/1392',
		'https://www.jstor.org/stable/2480681?seq=1',
		'https://www.jstor.org/stable/1521506?seq=1',
		'https://jeb.biologists.org/content/200/16/2209',
		'https://jeb.biologists.org/content/213/4/635',
		'https://www.jstor.org/stable/40596756?seq=1',
		'https://science.sciencemag.org/content/369/6511/1608',
		'https://science.sciencemag.org/content/327/5964/439',
		'https://jeb.biologists.org/content/219/18/2908',
		'http://dx.doi.org/10.1016/j.jphysparis.2008.10.017',
		'http://dx.doi.org/10.1126/science.abb6703',
		'http://dx.doi.org/10.1523/JNEUROSCI.0216-20.2020',
		'http://dx.doi.org/10.1016/j.cub.2020.06.044',
		'https://advances.sciencemag.org/content/6/31/eaba5168',
		'http://dx.doi.org/10.7554/eLife.52237',
		'http://dx.doi.org/10.1242/dmm.045971',
		'http://dx.doi.org/10.1242/jeb.215327',
		# 'http://connection.ebscohost.com/c/articles/9008131036/antifreeze-bees',  # bad link
		'https://elifesciences.org/articles/52187',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.71.011906',
		# 'https://iopscience.iop.org/article/10.1088/1748-3182/7/3/036014/pdf',  # PDF
		'http://dx.doi.org/10.1016/j.anbehav.2020.04.005',
		'https://science.sciencemag.org/content/293/5527/102',
		'http://dx.doi.org/10.7554/eLife.53370',
		'https://advances.sciencemag.org/content/5/3/eaau9183',
		'https://advances.sciencemag.org/content/1/10/e1500709',
		'http://dx.doi.org/10.1242/jeb.005694',
		'http://dx.doi.org/10.1126/science.aay6912',
		'https://www.scientificamerican.com/article/bumblebees-bite-plants-to-force-them-to-flower-seriously/',
		'http://dx.doi.org/10.1016/j.anbehav.2020.02.011',
		'https://science.sciencemag.org/content/315/5810/348',
		'https://jeb.biologists.org/content/221/4/jeb173047?etoc',
		'https://journals.aps.org/pre/abstract/10.1103/PhysRevE.76.031907',
		'https://www.jstor.org/stable/2398919?origin=crossref&seq=1',
		'http://dx.doi.org/10.1242/jeb.210807',
		'http://dx.doi.org/10.1126/sciadv.abb2307',
		# 'Bioinspiration & Biomimetics',  # bad link
		'http://dx.doi.org/10.7554/eLife.55195',
		'http://dx.doi.org/10.1242/jeb.219287',
		'http://dx.doi.org/10.1126/science.1188761',
		'http://dx.doi.org/10.1016/0034-5687(74)90044-9',
		'https://iopscience.iop.org/article/10.1088/1748-3182/5/2/026003/meta',
		'https://www.jstor.org/stable/2818333?seq=1',
		'http://dx.doi.org/10.1103/PhysRevLett.124.105302',
		'http://etheses.whiterose.ac.uk/9268/',
		'http://dx.doi.org/10.1242/jeb.219642',
		'https://jeb.biologists.org/content/212/22/3621',
		'https://science.sciencemag.org/content/315/5810/348?ijkey=e48b68c967890b299b6fb56dfa356ae675c12698&keytype2=tf_ipsecsha',
		'http://dx.doi.org/10.1016/j.cub.2020.07.046',
		# 'https://books.google.com/books?hl=en&lr=&id=zM0tG5ApO0UC&oi=fnd&pg=PR17&dq=ornithology+frank+b+gill&ots=T1uLIG2Dkl&sig=YAsfnO7UXxdnJa7Y6kE2pgtbtsY#v=onepage&q=ornithology%20frank%20b%20gill&f=false',  # bad link
		# 'https://www.cell.com/cell/pdf/S0092-8674(20)30567-5.pdf?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867420305675%3Fshowall%3Dtrue',  # PDF
		'https://jeb.biologists.org/content/223/20/jeb226654',
		'http://dx.doi.org/10.1016/j.cub.2020.03.071',
		'https://jeb.biologists.org/content/217/14/2548',
		'http://dx.doi.org/10.1088/1748-9326/ab9924',
		'https://www.researchgate.net/publication/273142268_A_new_study_on_the_structure_and_function_of_the_adhesive_organs_of_the_Old_World_sucker-footed_bat_Myzopoda_Myzopodidae_of_Madagascar',
		'http://dx.doi.org/10.1126/sciadv.aba1269',
		'http://dx.doi.org/10.1016/j.cub.2020.07.007',
		'https://elifesciences.org/articles/47682',
		'https://www.scielo.br/scielo.php?script=sci_arttext&pid=S0001-37141999000100001',
		'http://dx.doi.org/10.1523/JNEUROSCI.0241-20.2020',
		'https://jeb.biologists.org/content/212/21/3499',
		'http://dx.doi.org/10.1126/science.aba3203',
		'https://jeb.biologists.org/content/214/22/i.1',
		'http://dx.doi.org/10.1074/jbc.RA119.012281',
		'http://dx.doi.org/10.1242/jeb.037465',
		'http://dx.doi.org/10.1126/science.abb2978',
		'http://dx.doi.org/10.1016/j.algal.2020.101970',
		'https://elifesciences.org/articles/34862',
		# 'http://connection.ebscohost.com/c/articles/44322044/self-organization-escherichia-coli-chemotaxis-network-imaged-super-resolution-light-microscopy',  # bad link
		'https://science.sciencemag.org/content/358/6367/1172',
		'https://elifesciences.org/articles/52187',
		'https://qz.com/1465774/pyrosomes-the-unicorn-of-the-sea-wouldnt-exist-without-collaboration/',
		'http://dx.doi.org/10.7554/eLife.52716',
		'https://www.pnas.org/content/early/2010/10/11/1008768107/tab-article-info',
		'http://dx.doi.org/10.1016/j.matt.2020.09.023',
		'https://jeb.biologists.org/content/223/3/jeb214809',
		'https://jeb.biologists.org/content/219/22/3597',
		'https://jeb.biologists.org/content/215/2/279',
		'http://dx.doi.org/10.7554/eLife.55774',
		'https://www.researchgate.net/publication/239919503_Characteristics_and_Impacts_of_Annual_vs_Perennial_Systems',
		'https://www.jstor.org/stable/36378?seq=1',
		'http://dx.doi.org/10.1016/j.celrep.2020.108028',
		'http://dx.doi.org/10.1016/j.matt.2020.05.011',
		'http://dx.doi.org/10.1103/PhysRevX.10.021045',
		'http://dx.doi.org/10.1016/j.cels.2020.04.002',
		'https://advances.sciencemag.org/content/2/4/e1501630',
		'http://dx.doi.org/10.1016/j.cub.2020.07.005',
	]
	return urls