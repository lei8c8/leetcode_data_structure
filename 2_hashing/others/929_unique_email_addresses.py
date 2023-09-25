class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            splitted_email = email.split('@')
            local_name = splitted_email[0].replace('.', '')
            domain_name = splitted_email[1]
            if '+' in local_name:
                i = local_name.index('+')
                local_name = local_name[:i]
            final_email_address = local_name + '@' + domain_name
            unique_emails.add(final_email_address)

        return len(unique_emails)


if __name__ == '__main__':
    solution = Solution()
    test_data1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    result1 = solution.numUniqueEmails(test_data1)
    print(f"test 1 result: {result1}")
    test_data2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    result2 = solution.numUniqueEmails(test_data2)
    print(f"test 2 result: {result2}")