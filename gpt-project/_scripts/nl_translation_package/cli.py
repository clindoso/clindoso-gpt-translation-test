import argparse
from nl_translation_package.translator.main import main as tr_main
from nl_translation_package.tm_aligner.tm_aligner import main as al_main

def main():
    # Create a top-level parser
    parser = argparse.ArgumentParser(prog='nl_translation_project', description='Translate articles, align TM segments, and extract prompts to fine tune a ChatGPT model.')
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='')

    # Create a parser for the "translate" command
    parser_translate = subparsers.add_parser('translate', help='Translate Help Center articles')
    parser_translate.add_argument('source', type=str, help='Source path of article to translate')
    parser_translate.add_argument('--lang', type=str, default='nl', help='Target language for translation, default is Dutch')
    parser_translate.set_defaults(func=tr_main)

    # Create a parser for the "align" comand
    parser_align = subparsers.add_parser('align', help='Align segments from Help Center articles')
    parser_align.add_argument('--lang', type=str, default='nl', help='Target language for translation memory, default is Dutch')
    parser_align.set_defaults(func=al_main)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()