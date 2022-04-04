# Generated from /home/ilya/work/cdm8e/ORiGinalASM/assembler/AsmParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AsmParser import AsmParser
else:
    from AsmParser import AsmParser

# This class defines a complete generic visitor for a parse tree produced by AsmParser.

class AsmParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AsmParser#program.
    def visitProgram(self, ctx:AsmParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#absoluteSection.
    def visitAbsoluteSection(self, ctx:AsmParser.AbsoluteSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#relocatableSection.
    def visitRelocatableSection(self, ctx:AsmParser.RelocatableSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#templateSection.
    def visitTemplateSection(self, ctx:AsmParser.TemplateSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#asect_header.
    def visitAsect_header(self, ctx:AsmParser.Asect_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#rsect_header.
    def visitRsect_header(self, ctx:AsmParser.Rsect_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#tplate_header.
    def visitTplate_header(self, ctx:AsmParser.Tplate_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#section_body.
    def visitSection_body(self, ctx:AsmParser.Section_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#code_block.
    def visitCode_block(self, ctx:AsmParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#break_statement.
    def visitBreak_statement(self, ctx:AsmParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#continue_statement.
    def visitContinue_statement(self, ctx:AsmParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#standaloneLabel.
    def visitStandaloneLabel(self, ctx:AsmParser.StandaloneLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#instructionLine.
    def visitInstructionLine(self, ctx:AsmParser.InstructionLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#label_declaration.
    def visitLabel_declaration(self, ctx:AsmParser.Label_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#arguments.
    def visitArguments(self, ctx:AsmParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#conditional.
    def visitConditional(self, ctx:AsmParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#conditions.
    def visitConditions(self, ctx:AsmParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#connective_condition.
    def visitConnective_condition(self, ctx:AsmParser.Connective_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#condition.
    def visitCondition(self, ctx:AsmParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#else_clause.
    def visitElse_clause(self, ctx:AsmParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#branch_mnemonic.
    def visitBranch_mnemonic(self, ctx:AsmParser.Branch_mnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#conjunction.
    def visitConjunction(self, ctx:AsmParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#while_loop.
    def visitWhile_loop(self, ctx:AsmParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#while_condition.
    def visitWhile_condition(self, ctx:AsmParser.While_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#until_loop.
    def visitUntil_loop(self, ctx:AsmParser.Until_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#save_restore_statement.
    def visitSave_restore_statement(self, ctx:AsmParser.Save_restore_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#save_statement.
    def visitSave_statement(self, ctx:AsmParser.Save_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#restore_statement.
    def visitRestore_statement(self, ctx:AsmParser.Restore_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#argument.
    def visitArgument(self, ctx:AsmParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#template_field.
    def visitTemplate_field(self, ctx:AsmParser.Template_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#label.
    def visitLabel(self, ctx:AsmParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#instruction.
    def visitInstruction(self, ctx:AsmParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#string.
    def visitString(self, ctx:AsmParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#register.
    def visitRegister(self, ctx:AsmParser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#character.
    def visitCharacter(self, ctx:AsmParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#number.
    def visitNumber(self, ctx:AsmParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmParser#name.
    def visitName(self, ctx:AsmParser.NameContext):
        return self.visitChildren(ctx)



del AsmParser