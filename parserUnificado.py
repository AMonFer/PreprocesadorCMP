from ChainOfResp import Handler, LL1Parser, LR0Parser, LR1Parser, RecursiveDescentParser


def unified_parser(input_string):
    # Set up the chain
    handler = Handler()
    ll1_parser = LL1Parser(handler)
    lr0_parser = LR0Parser(handler)
    ll1_parser._successor = lr0_parser
    lr1_parser = LR1Parser(handler)
    lr0_parser._successor = lr1_parser
    recursive_parser = RecursiveDescentParser(handler)
    lr1_parser._successor = recursive_parser

    # input_string = 'int a = 7 ;'  # Ejemplo de cadena de entrada

    ll1_parser.handle(input_string)
    ll1_parser.successor.handle(input_string)


# unified_parser()