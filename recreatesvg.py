from svgpathtools import svg2paths, Path, Line
import logging
import os

def calculate_complexity(svg_file):
    paths, _ = svg2paths(svg_file)
    complexity = sum(len(path) for path in paths)
    return complexity

def simplify_path(path, target_complexity):
    if len(path) <= target_complexity:
        return path

    step = len(path) / target_complexity
    simplified_segments = [path[int(i * step)] for i in range(target_complexity)]

    simplified_path = Path(*simplified_segments)
    return simplified_path

def rescale_and_translate_paths(paths, target_min=(0, 0), target_max=(100, 100)):
    all_points = [seg.start for path in paths for seg in path] + [seg.end for path in paths for seg in path]
    min_x = min(p.real for p in all_points)
    max_x = max(p.real for p in all_points)
    min_y = min(p.imag for p in all_points)
    max_y = max(p.imag for p in all_points)

    scale_x = (target_max[0] - target_min[0]) / (max_x - min_x)
    scale_y = (target_max[1] - target_min[1]) / (max_y - min_y)
    scale = min(scale_x, scale_y)

    new_paths = []
    for path in paths:
        new_segments = [
            Line(
                complex(target_min[0] + (seg.start.real - min_x) * scale, target_min[1] + (seg.start.imag - min_y) * scale),
                complex(target_min[0] + (seg.end.real - min_x) * scale, target_min[1] + (seg.end.imag - min_y) * scale)
            )
            for seg in path
        ]
        new_paths.append(Path(*new_segments))

    return new_paths

def process_svg(input_svg, output_svg, scenario1_complexity):
    max_complexity = scenario1_complexity * 2

    paths, attributes = svg2paths(input_svg)
    
    simplified_paths = [simplify_path(path, max_complexity) for path in paths]
    final_paths = rescale_and_translate_paths(simplified_paths)

    save_svg(final_paths, attributes, output_svg)
    logging.info(f"Archivo guardado: {output_svg}")

def save_svg(paths, attributes, filename):
    with open(filename, 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n')
        for path, attr in zip(paths, attributes):
            path_d = path.d()  # Genera la cadena `d` correctamente
            style_attr = attr.get('style', '')  # Asegurarse de incluir `style` si está presente
            f.write(f'  <path d="{path_d}" style="{style_attr}" />\n')
        f.write('</svg>')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    scenario1_svg = "app/src/svg_images/scenario1.svg"
    scenario1_complexity = calculate_complexity(scenario1_svg)*5

    scenario2_svg = "app/src/svg_images/scenario2.svg"
    output_svg = "app/src/svg_images/scenario2_simplified.svg"
    process_svg(scenario2_svg, output_svg, scenario1_complexity)

