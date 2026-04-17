class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result=set()
        for email in emails:
            mail,domain=email.split('@')
            mail=mail.replace('.','')
            if '+' in mail:
                mail=mail[:mail.index('+')]
            result.add(mail+"@"+domain)
        return len(result)