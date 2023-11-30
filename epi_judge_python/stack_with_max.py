from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def empty(self) -> bool:
        # TODO - you fill in here.
        if len(self.data) == 0:
            return True
        else:
            return False

    def max(self) -> int:
        # TODO - you fill in here.
        print(self.max)
        return self.max

    def pop(self) -> int:
        # TODO - you fill in here.
        print(self.data)
        if (len(self.data) == 0):
            return None
        tmp = self.data.pop()
        if tmp == self.max:
            if len(self.data) == 0:
                self.max = None
            else:
                self.max = self.data[-1]
                for i in range(len(self.data) - 1):
                    if self.data[i] > self.max:
                        self.max = self.data[i]
        return tmp

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        print(self.data)
        if self.max == None:
            self.max = x
        elif x > self.max:
            self.max = x
        self.data.append(x)

    data = []
    max = None


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
