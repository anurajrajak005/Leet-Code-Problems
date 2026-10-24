class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        tmp1 = arriveAlice.split("-")
        tmp2 = leaveAlice.split("-")
        m1, d1 = int(tmp1[0]), int(tmp1[1])
        m2, d2 = int(tmp2[0]), int(tmp2[1])
        a1 = sum(days[:m1]) + d1
        l1 = sum(days[:m2]) + d2

        tmp1 = arriveBob.split("-")
        tmp2 = leaveBob.split("-")
        m1, d1 = int(tmp1[0]), int(tmp1[1])
        m2, d2 = int(tmp2[0]), int(tmp2[1])
        a2 = sum(days[:m1]) + d1
        l2 = sum(days[:m2]) + d2

        diff = min(l1, l2) - max(a1, a2) + 1

        return max(diff, 0)