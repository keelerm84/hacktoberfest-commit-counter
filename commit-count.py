import datetime


class Specification:
    def is_satisified_by(candidate):
        raise NotImplementedError('And must be implemented')

    def is_not(self, spec):
        raise NotImplementedError('And must be implemented')

    def and_if(self, spec):
        raise NotImplementedError('And must be implemented')

    def or_if(self, spec):
        raise NotImplementedError('And must be implemented')


class CompositeSpecification(Specification):
    def is_not(self):
        return NotSpecification(self)

    def and_if(self, spec):
        return AndSpecification(self, spec)

    def or_if(self, spec):
        return OrSpecification(self, spec)


class NotSpecification(CompositeSpecification):
    def __init__(self, spec):
        self.spec = spec

    def is_satisified_by(self, candidate):
        return not candidate.is_satisified_by(candidate)


class AndSpecification(CompositeSpecification):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def is_satisified_by(self, candidate):
        return self.lhs.is_satisified_by(candidate) and self.rhs.is_satisified_by(candidate)


class OrSpecification(CompositeSpecification):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def is_satisified_by(self, candidate):
        return self.lhs.is_satisified_by(candidate) or self.rhs.is_satisified_by(candidate)


class PushEventSpecification(CompositeSpecification):
    def is_satisified_by(self, candidate):
        return candidate['type'] == "PushEvent"


class CreatedOnOrAfterSpecification(CompositeSpecification):
    def __init__(self, starting_date):
        self.starting_date = starting_date

    def is_satisified_by(self, candidate):
        commit_date = datetime.datetime.strptime(candidate['created_at'].split('T')[0], "%Y-%m-%d")

        return self.starting_date <= commit_date


