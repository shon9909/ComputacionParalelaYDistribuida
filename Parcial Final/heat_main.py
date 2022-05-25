from __future__ import print_function
import time
import argparse
import heat

def main(heat_lib, input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1,
         timesteps=200, image_interval=4000, filename='heat.txt', num_iter=0):

    # Initialise the temperature field
    field, field0 = heat_lib.init_fields(input_file)

    print("Heat equation solver")
    print("Diffusion constant: {}".format(a))
    print("Input file: {}".format(input_file))
    print("Parameters")
    print("----------")
    print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
                                             dx, dy))
    print("  time steps={}  image interval={}".format(timesteps,
                                                      image_interval))

    # Plot/save initial field
    heat_lib.write_field(field, 0)
    # Iterate
    t0 = time.time_ns()
    heat_lib.iterate(field, field0, a, dx, dy, timesteps, image_interval)
    t1 = time.time_ns()
    # Plot/save final field
    heat_lib.write_field(field, timesteps)

    with open(filename, 'a') as file:
        file.write(f'{input_file} #{num_iter} in {t1-t0} ns\n')

    print(f'Simulation finished in {t1-t0} ns')


if __name__ == '__main__':

    lib_dict = {
        'heat': heat,
        # 'heatCy': heatCy,
    }
    bottles_dict = {
        'bottle': 'bottle.dat',
        'bottle_medium': 'bottle_medium.dat',
        'bottle_large': 'bottle_large.dat',
    }
    for lib in lib_dict:
        for bottle in bottles_dict:
            for i in range(4):
                # Process command line arguments
                filename = f'/outputs/'
                parser = argparse.ArgumentParser(description='Heat equation')
                parser.add_argument('-dx', type=float, default=0.01,
                                    help='grid spacing in x-direction')
                parser.add_argument('-dy', type=float, default=0.01,
                                    help='grid spacing in y-direction')
                parser.add_argument('-a', type=float, default=0.5,
                                    help='diffusion constant')
                parser.add_argument('-n', type=int, default=200,
                                    help='number of time steps')
                parser.add_argument('-i', type=int, default=4000,
                                    help='image interval')
                parser.add_argument('-f', type=str, default=bottles_dict[bottle],
                                    help='input file')

                args = parser.parse_args()

                main(lib_dict[lib], args.f, args.a,
                     args.dx, args.dy, args.n, args.i, filename=filename, num_iter=i)