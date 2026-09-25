def place_ship(length, player):

    while True:
        try:
            coordinate = input(f"Place your Carrier({length} spaces long) by entering the first coordinate(example: C3): ").title().strip()
            coordinates_list = list(coordinate)
            row_value = ord(coordinates_list[0])

            if len(coordinates_list) == 3:
                rlist = [coordinates_list[1], coordinates_list[2]]
                column = "".join(rlist)
            else:
                column = coordinates_list[1]
            
            column_num = int(column)

        except:
            print("That is not an option!!!")
        else:
            if len(coordinate) >= 2 and len(coordinate) <= 3 and column_num >= 1 and column_num <= 10 and row_value >= 65 and row_value <= 74:
                row_value -= 65
                row_value = row_value * 10
                start_coord = row_value + column_num
                break
            else:
                print("THAT'S NOT AN OPTION!!!")

    # End coordinate (five long)
    while True:
        try:
            direction = input("Finish placing your carrier by entering the direction you want it to face(R for right, L for left, U for up, D for down): ").strip().capitalize()
        except:
            print("THAT'S NOT AN OPTION!!!")
        else:

            #RIGHT

            if direction == "R":
                end_coord = row_value + column_num + 4
                start_list = list(str(start_coord))
                end_list = list(str(end_coord))

                if len(start_list) == 1 and len(end_list) == 1:
                    start_num = 0
                    end_num = 0
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = 0
                    end_num = end_list[0]
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = 0
                elif len(start_list) == 2 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = end_list[0]


                if end_num == start_num:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord + 1)
                        p1_ship_coords.append(start_coord + 2)
                        p1_ship_coords.append(start_coord + 3)
                        p1_ship_coords.append(start_coord + 4)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord + 1)
                        p2_ship_coords.append(start_coord + 2)
                        p2_ship_coords.append(start_coord + 3)
                        p2_ship_coords.append(start_coord + 4)
                    break
                else:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")

            #LEFT

            elif direction == "L":
                end_coord = row_value + column_num - 4
                start_list = list(str(start_coord))
                end_list = list(str(end_coord))

                if len(start_list) == 1 and len(end_list) == 1:
                    start_num = 0
                    end_num = 0
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = 0
                    end_num = end_list[0]
                elif len(start_list) == 1 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = 0
                elif len(start_list) == 2 and len(end_list) == 2:
                    start_num = start_list[0]
                    end_num = end_list[0]


                if end_num == start_num:
                    if player == 1:
                        p1_ship_coords.append(end_coord)
                        p1_ship_coords.append(end_coord + 1)
                        p1_ship_coords.append(end_coord + 2)
                        p1_ship_coords.append(end_coord + 3)
                        p1_ship_coords.append(end_coord + 4)
                    elif player == 2:
                        p2_ship_coords.append(end_coord)
                        p2_ship_coords.append(end_coord + 1)
                        p2_ship_coords.append(end_coord + 2)
                        p2_ship_coords.append(end_coord + 3)
                        p2_ship_coords.append(end_coord + 4)
                    break
                else:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
            
            #DOWN

            elif direction == "D":
                end_coord = row_value + column_num + 40
                
                if end_coord > 100 or end_coord < 0:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
                else:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord - 10)
                        p1_ship_coords.append(start_coord - 20)
                        p1_ship_coords.append(start_coord - 30)
                        p1_ship_coords.append(start_coord - 40)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord - 10)
                        p2_ship_coords.append(start_coord - 20)
                        p2_ship_coords.append(start_coord - 30)
                        p2_ship_coords.append(start_coord - 40)
                    break
                    
            #UP

            elif direction == "U":
                end_coord = row_value + column_num - 40
                
                if end_coord > 100 or end_coord < 0:
                    print("YOUR SHIP CANNOT CUT INTO THE SIDE OF THE BOARD!!!")
                else:
                    if player == 1:
                        p1_ship_coords.append(start_coord)
                        p1_ship_coords.append(start_coord + 10)
                        p1_ship_coords.append(start_coord + 20)
                        p1_ship_coords.append(start_coord + 30)
                        p1_ship_coords.append(start_coord + 40)
                    elif player == 2:
                        p2_ship_coords.append(start_coord)
                        p2_ship_coords.append(start_coord + 10)
                        p2_ship_coords.append(start_coord + 20)
                        p2_ship_coords.append(start_coord + 30)
                        p2_ship_coords.append(start_coord + 40)
                    break
                    
            else:
                print("THAT'S NOT AN OPTION!!!")
