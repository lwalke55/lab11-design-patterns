from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an empty value."""
        textarr = text.split()
        initials = ""
        for i in textarr:
            counter = 0
            for j in i:
                if j.isalnum():
                    if i == textarr[len(textarr) - 1]:
                        initials += j + "."
                        break
                    else:
                        initials += j + ". "
                        break
                else:
                    initials += j
                    counter += 1
        initials = initials.upper()

        return initials

    def validate(self, params: Dict = None) -> None:
        """initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize