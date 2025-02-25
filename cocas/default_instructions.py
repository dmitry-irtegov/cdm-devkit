from cocas.ast_nodes import *
from cocas.default_code_segments import CodeSegmentsInterface


class TargetInstructionsInterface:
    @staticmethod
    def assemble_instruction(line: InstructionNode, temp_storage) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    @staticmethod
    def finish(temp_storage: dict):
        return

    @staticmethod
    def make_branch_instruction(location: CodeLocation, branch_mnemonic: str, label_name: str, inverse: bool) \
            -> list[CodeSegmentsInterface.CodeSegment]:
        pass

    assembly_directives: dict
