def main():
    seed_soil_range = []
    soil_fert_range = []
    fert_water_range = []
    water_light_range = []
    light_temp_range = []
    temp_hum_range = []
    hum_loc_range = []

    with open('5.in') as f:
        seed_line = f.readline().strip()
        seeds = seed_line.split(' ')[1:]
        seeds = list(map(int, seeds))
        while True:
            line = f.readline()
            if line == '':
                break
            if line.startswith('seed-to-soil'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    seed_soil_s = list(map(int, line.split()))
                    soil_start, seed_start, count = seed_soil_s
                    seed_soil_range.append((seed_start, seed_start + count - 1,  soil_start - seed_start))
                    line = f.readline().strip()
            if line.startswith('soil-to-fertilizer'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    soil_fert_s = list(map(int, line.split()))
                    fert_start, soil_start, count = soil_fert_s
                    soil_fert_range.append((soil_start, soil_start + count - 1, fert_start - soil_start))
                    line = f.readline().strip()
            if line.startswith('fertilizer-to-water'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    fert_water_s = list(map(int, line.split()))
                    water_start, fert_start, count = fert_water_s
                    fert_water_range.append((fert_start, fert_start + count - 1, water_start - fert_start))
                    line = f.readline().strip()
            if line.startswith('water-to-light'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    water_light_s = list(map(int, line.split()))
                    light_start, water_start, count = water_light_s
                    water_light_range.append((water_start, water_start + count - 1, light_start - water_start))
                    line = f.readline().strip()
            if line.startswith('light-to-temperature'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    light_temp_s = list(map(int, line.split()))
                    temp_start, light_start, count = light_temp_s
                    light_temp_range.append((light_start, light_start + count - 1, temp_start - light_start))
                    line = f.readline().strip()
            if line.startswith('temperature-to-humidity'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    temp_hum_s = list(map(int, line.split()))
                    hum_start, temp_start, count = temp_hum_s
                    temp_hum_range.append((temp_start, temp_start + count - 1, hum_start - temp_start))
                    line = f.readline().strip()
            if line.startswith('humidity-to-location'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    hum_loc_s = list(map(int, line.split()))
                    loc_start, hum_start, count = hum_loc_s
                    hum_loc_range.append((hum_start, hum_start + count - 1, loc_start - hum_start))
                    line = f.readline().strip()
            
    soils = []
    for seed in seeds:
        for soil in seed_soil_range:
            if soil[0] <= seed <= soil[1]:
                soils.append(seed + soil[2])
                break
        else:
            soils.append(seed)
    ferts = []
    for soil in soils:
        for fert in soil_fert_range:
            if fert[0] <= soil <= fert[1]:
                ferts.append(soil + fert[2])
                break
        else:
            ferts.append(soil)
    waters = []
    for fert in ferts:
        for water in fert_water_range:
            if water[0] <= fert <= water[1]:
                waters.append(fert + water[2])
                break
        else:
            waters.append(fert)
    lights = []
    for water in waters:
        for light in water_light_range:
            if light[0] <= water <= light[1]:
                lights.append(water + light[2])
                break
        else:
            lights.append(water)
    temps = []
    for light in lights:
        for temp in light_temp_range:
            if temp[0] <= light <= temp[1]:
                temps.append(light + temp[2])
                break
        else:
            temps.append(light)
    hums = []
    for temp in temps:
        for hum in temp_hum_range:
            if hum[0] <= temp <= hum[1]:
                hums.append(temp + hum[2])
                break
        else:
            hums.append(temp)
    locs = []
    for hum in hums:
        for loc in hum_loc_range:
            if loc[0] <= hum <= loc[1]:
                locs.append(hum + loc[2])
                break
        else:
            locs.append(hum)
    print(min(locs))


    ##########################################
    ################ PART 2 ##################
    ##########################################

    seed_soil_range = []
    soil_fert_range = []
    fert_water_range = []
    water_light_range = []
    light_temp_range = []
    temp_hum_range = []
    hum_loc_range = []

    with open('5.in') as f:
        seed_line = f.readline().strip()
        seeds = seed_line.split(' ')[1:]
        seeds = list(map(int, seeds))
        while True:
            line = f.readline()
            if line == '':
                break
            if line.startswith('seed-to-soil'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    seed_soil_s = list(map(int, line.split()))
                    soil_start, seed_start, count = seed_soil_s
                    seed_soil_range.append((soil_start, soil_start + count - 1,  soil_start - seed_start))
                    line = f.readline().strip()
            if line.startswith('soil-to-fertilizer'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    soil_fert_s = list(map(int, line.split()))
                    fert_start, soil_start, count = soil_fert_s
                    soil_fert_range.append((fert_start, fert_start + count - 1, fert_start - soil_start))
                    line = f.readline().strip()
            if line.startswith('fertilizer-to-water'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    fert_water_s = list(map(int, line.split()))
                    water_start, fert_start, count = fert_water_s
                    fert_water_range.append((water_start, water_start + count - 1, water_start - fert_start))
                    line = f.readline().strip()
            if line.startswith('water-to-light'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    water_light_s = list(map(int, line.split()))
                    light_start, water_start, count = water_light_s
                    water_light_range.append((light_start, light_start + count - 1, light_start - water_start))
                    line = f.readline().strip()
            if line.startswith('light-to-temperature'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    light_temp_s = list(map(int, line.split()))
                    temp_start, light_start, count = light_temp_s
                    light_temp_range.append((temp_start, temp_start + count - 1, temp_start - light_start))
                    line = f.readline().strip()
            if line.startswith('temperature-to-humidity'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    temp_hum_s = list(map(int, line.split()))
                    hum_start, temp_start, count = temp_hum_s
                    temp_hum_range.append((hum_start, hum_start + count - 1, hum_start - temp_start))
                    line = f.readline().strip()
            if line.startswith('humidity-to-location'):
                line = f.readline().strip()
                while line != '':
                    line = line.strip()
                    hum_loc_s = list(map(int, line.split()))
                    loc_start, hum_start, count = hum_loc_s
                    hum_loc_range.append((loc_start, loc_start + count - 1, loc_start - hum_start))
                    line = f.readline().strip()
    seeds_input = seeds
    seeds = []
    for i in range(0, len(seeds_input), 2):
        seeds.append((seeds_input[i], seeds_input[i + 1]))

    def check(location):
        for loc_start, loc_end, diff in hum_loc_range:
            if loc_start <= location <= loc_end:
                humidity = location - diff
                break
        else:
            humidity = location
        for hum_start, hum_end, diff in temp_hum_range:
            if hum_start <= humidity <= hum_end:
                temperature = humidity - diff
                break
        else:
            temperature = humidity
        for temp_start, temp_end, diff in light_temp_range:
            if temp_start <= temperature <= temp_end:
                light = temperature - diff
                break
        else:
            light = temperature
        for light_start, light_end, diff in water_light_range:
            if light_start <= light <= light_end:
                water = light - diff
                break
        else:
            water = light
        for water_start, water_end, diff in fert_water_range:
            if water_start <= water <= water_end:
                fertilizer = water - diff
                break
        else:
            fertilizer = water
        for fert_start, fert_end, diff in soil_fert_range:
            if fert_start <= fertilizer <= fert_end:
                soil = fertilizer - diff
                break
        else:
            soil = fertilizer
        for soil_start, soil_end, diff in seed_soil_range:
            if soil_start <= soil <= soil_end:
                seed = soil - diff
                break
        else:
            seed = soil

        for seed_start, seed_range in seeds:
            if seed_start <= seed < seed_start + seed_range:
                return True
        return False

    left = 5467036
    right = 0
    for _, max_loc, _ in hum_loc_range:
        right = max(right, max_loc)
    
    for i in range(left, right + 1):
        if check(i):
            print(i)
            break


if __name__ == "__main__":
    main()
