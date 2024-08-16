import ast

#List of input files path
input_files = [
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt21.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt22.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt23.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt24.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt25.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt31.txt',
    r'C:\Users\james\OneDrive\Desktop\DataSampleTest\logt32.txt'
]

#Output file path
output_file = r'C:\Users\james\OneDrive\Desktop\DataSampleTest\parse_log.txt'

#Prepare output file
with open(output_file, 'w') as output:
    output.write('Mac\tSessionMainMenu\tAppName\tLogID\tEvent\tItemID\tRealTimePlaying\n')

    #Process each file in the input list
    for input_file in input_files:
        with open(input_file, 'r') as input:
            data_line = input.readlines()

        for line in data_line:
            try:
                #Parse data
                data = ast.literal_eval(line.strip())

                #Extract relevant fields
                mac = data.get('Mac', '')
                session_main_menu = data.get('SessionMainMenu', '')
                app_name = data.get('AppName', '')
                log_id = data.get('LogId', '')
                event = data.get('Event', '')
                item_id = data.get('ItemId', '')
                real_time_playing = data.get('RealTimePlaying', '')

                 # Write the parsed data to the output file in tab-separated format
                output.write(f"{mac}\t{session_main_menu}\t{app_name}\t{log_id}\t{event}\t{item_id}\t{real_time_playing}\n")

            except (ValueError, SyntaxError) as e:
                print(f"Skipping line due to JSON parsing error in {input_file}: {e}")

print(f"Parsed log saved to {output_file}")


