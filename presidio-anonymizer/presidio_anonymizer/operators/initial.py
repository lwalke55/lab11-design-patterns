from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an empty value."""
        textarr = text.split()
        initials = ""
        for i in textarr:
            #if i[0][0] == char:
            counter = 0
            for j in textarr[len(textarr) - 1][counter]:
                if j.isalnum():
                    if i == textarr[len(textarr) - 1]:
                        initials += i[0] + "."
                    else:
                        initials += i[0] + ". "
                counter += 1
                if counter == textarr[len(textarr) - 1]:
                    break
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