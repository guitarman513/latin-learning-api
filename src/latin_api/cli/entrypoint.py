import argparse

from latin_api.api.webapp import init as entrypoint_run_webapp

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("_subparser_entrypoint_func", action="store_const", help=argparse.SUPPRESS, const=lambda _: parser.print_help())  # In case entrypoint is called with no args

    subparser = parser.add_subparsers()  # To this subparser we will add a parser for `run-webapp` which will start the API

    parser_to_run_webapp = subparser.add_parser('run-webapp')
    
    # Create an arg for the entrypoint func. Default is `entrypoint_run_webapp`.
    parser_to_run_webapp.add_argument(
        "_subparser_entrypoint_func",
        action="store_const",
        help=argparse.SUPPRESS,
        const=lambda args: entrypoint_run_webapp(args.host, args.port)
    )

    # Add parser for host 
    parser_to_run_webapp.add_argument(
        "--host",
        help='The IP or hostname on which the application should run',
        type=str,
        default='0.0.0.0'
    )

    # Add parser for port
    parser_to_run_webapp.add_argument(
        "--port",
        help='The port on which the application should run',
        type=int,
        default=8080
    )

    args = parser.parse_args()

    entrypoint = vars(args).pop('_subparser_entrypoint_func')  # This is a slick way to return `entrypoint_run_webapp`

    return entrypoint(args)  # This runs `entrypoint_run_webapp` with the parsed args

if __name__ == '__main__':
    main()