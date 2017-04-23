import service.filesystem_dao as filesystem_dao
import data_manilpulation.generic_manipulation as generic_manipulation
import chart.line_chart as line_chart

tracks_ids = ["58fa0540268d1b08a4497422", "58fa053e268d1b08a449733a", "58f99cd7268d1b08a4496ad7", "58f841b9268d1b08a4487e2e", "58f8408d268d1b08a4487995", "58f84089268d1b08a44874ea", "58f84081268d1b08a448701e", "58f63148268d1b08a445dc48", "58f5b14b268d1b08a445d910", "58efec10268d1b08a43e2b20", "58efec0e268d1b08a43e26ed", "58efebd2268d1b08a43e22c9", "58efebce268d1b08a43e1f6b", "58efebcb268d1b08a43e1c07", "58efebc8268d1b08a43e1924", "58efebc5268d1b08a43e1608", "58efebc2268d1b08a43e11d5", "58efebbf268d1b08a43e0de7", "58efebbb268d1b08a43e08e2", "58efebb7268d1b08a43e056f", "58efebb3268d1b08a43e01d5", "58efebaf268d1b08a43dfe26", "58efebab268d1b08a43df9f6", "58efeba6268d1b08a43df539", "58efeba1268d1b08a43df03d", "58efeb9c268d1b08a43ded27", "58efeb97268d1b08a43dea3b", "58efeb92268d1b08a43de60e", "58efeb8d268d1b08a43de1d8", "58efeb86268d1b08a43ddd48", "58efeb7f268d1b08a43dd825", "58efeb78268d1b08a43dd27e", "58efeb71268d1b08a43dcbf3", "58efeb68268d1b08a43dc54d", "58efeb61268d1b08a43dbefb", "58efeb57268d1b08a43db94e", "58efeb4d268d1b08a43dae94", "58efeb2f268d1b08a43da49a", "58ee7edd268d1b08a43b8dbf", "58e69a37268d1b08a4e04992", "58e6990c268d1b08a4e00f0e", "58e695b6268d1b08a4df66cc", "58e50c89268d1b08a4d4e2d9", "58e50c83268d1b08a4d4e227", "58e3ed25268d1b08a4adcf20", "58e3ed22268d1b08a4adca6f", "58e3ed1e268d1b08a4adc5a9", "58e3ed1a268d1b08a4adc0d7", "58e3ed13268d1b08a4adb647", "58e3ed0c268d1b08a4adaf77", "58e3ed04268d1b08a4adabda", "58e3ecfe268d1b08a4ada507", "58e3ecf7268d1b08a4ad9f87", "58e3eced268d1b08a4ad9959", "58e3ece8268d1b08a4ad9393", "58e3ecdc268d1b08a4ad8e46", "58dd157d268d1b08a40db9b7", "58dd156d268d1b08a40d9fcd", "58db5ed5268d1b091fd891fb", "58db5ed2268d1b091fd88d6e", "58db5ed0268d1b091fd88926", "58db5ece268d1b091fd8848a", "58db5ecb268d1b091fd87f34", "58db5ec7268d1b091fd879ae", "58db5ec3268d1b091fd874c4", "58db5ebc268d1b091fd86f59", "58db5eaf268d1b091fd866ee", "58d92507268d1b091fd607dd", "58d91c5b268d1b091fd603f0", "58d42641268d1b091f2a2047", "58d425f7268d1b091f2a160f", "58d425ed268d1b091f2a1547", "58d425ce268d1b091f2a0160", "58d425a1268d1b091f29fc74", "58d4258e268d1b091f29fc41", "58cd2308268d1b091f16516e", "58cc2ff7268d1b091f156169", "58c24888268d1b08d804f99a", "58c245f1268d1b08d804f1b1", "58c24559268d1b08d804eaee", "58c24514268d1b08d804e470", "58c244b7268d1b08d804ddf5", "58c24106268d1b08d804d789", "58c240c1268d1b08d804d006", "58c23fe8268d1b08d804c943", "58c23b61268d1b08d804c2f8", "58c239fe268d1b08d804bc9b", "58ad9fcf268d1b08d85b2e5e", "58ad9ad8268d1b08d85aa19b", "58a7306e268d1b08d879081b", "58a7306c268d1b08d87907db", "58a7306a268d1b08d8790714", "58a73064268d1b08d87906fe", "58a73059268d1b08d8790172", "58a7303a268d1b08d878fab7", "58a5e7ed268d1b08d8781438", "58a5e7e3268d1b08d87811b2", "58a5e7d8268d1b08d8780ddc", "58a5d5c7268d1b08d878093c", "58a5d5b4268d1b08d8780632"]

#envirocar_service.retrieve_track_ids_from_first_page();
#first_track = tracks_ids[0]
#list(map(lambda x: write_to_file(x), tracks_ids))
#print("deu deu deu")

#all_tracks = list(map(lambda x: read_from_file_as_json(x), tracks_ids))
#all_intervals = list(map(lambda track: compute_duration_of_a_track(track), all_tracks))
#print(all_intervals)

#write_list_as_simple_csv(all_intervals, 'data_integration/duration.csv')

#all_tracks = list(map(lambda x: filesystem_dao.read_from_file_as_json(x), tracks_ids))
#all_speeds = list(map(lambda track: generic_manipulation.extract_speed(track), all_tracks))
#line_chart.do_the_plotting(all_speeds[40])

all_tracks = list(map(lambda x: filesystem_dao.read_from_file_as_json(x), tracks_ids))

position = generic_manipulation.extract_position(all_tracks[80])
algo = list(map(lambda x: {'lat': x[1], 'lng': x[0]}, position))
print(algo)



#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[10]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[20]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[30]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[40]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[50]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[60]))
#line_chart.line_plotting_two_dimensions(generic_manipulation.extract_position(all_tracks[70]))
