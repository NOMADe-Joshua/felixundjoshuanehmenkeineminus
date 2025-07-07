from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomadworkshop.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class joshuashirnExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomadworkshop.parsers.joshuashirn_batch_parser import joshuashirnExperimentParser

        return joshuashirnExperimentParser(**self.model_dump())


class joshuashirnParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomadworkshop.parsers.joshuashirn_measurement_parser import joshuashirnParser

        return joshuashirnParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


joshuashirn_experiment_parser_entry_point = joshuashirnExperimentParserEntryPoint(
    name='joshuashirnExperimentParserEntryPoint',
    description='joshuashirn experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


joshuashirn_parser_entry_point = joshuashirnParserEntryPoint(
    name='joshuashirnParserEntryPoint',
    description='joshuashirn parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
