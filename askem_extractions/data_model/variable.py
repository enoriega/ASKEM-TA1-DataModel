from typing import Optional

from pydantic import BaseModel

from askem_extractions.data_model import Equation
from askem_extractions.data_model.data_column import DataColumn
from askem_extractions.data_model.dkg_concept import DKGConcept
from askem_extractions.data_model.paper import Paper
from askem_extractions.data_model.variable_metadata import VariableMetadata


class Variable(BaseModel):
    """ Represents an extracted variable/identifier """
    id: str
    name: str
    metadata: list[VariableMetadata] = []    # Any additional metadata goes here
    dkg_groundings: list[DKGConcept]
    column: list[DataColumn] = []            # Default value of empty list
    paper: Optional[Paper]
    equations: list[Equation] = []           # Optional equations to which this variable is associated

    class Config:
        schema_extra = {
            '$id': "#/definitions/Variable"
        }