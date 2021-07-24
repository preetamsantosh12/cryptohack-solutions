## DATA FORMATS
___
##### CERTainly not

can use openssl cli to find modulus

```bash
 openssl x509 -inform DER -in "path to the .der file" -text -noout -modulus
```

convert result modulus form hex to int

---

##### SSH keys
parse the ssh key and convert he modulus from hex to int

---

##### Transparency

1. Using [CyberChef](https://gchq.github.io/CyberChef/):
   convert the pem to hex , decode the hex, and encode that in sha 256
   the resultant string is the sha256 fingerprint for the subdomain
   <br>
2. Using openssl cli , to find the fingerprint
   ```bash
   openssl pkey -outform der -pubin -in "path to .pem file" | sha256sum
   ```
   search for the certificates https://censys.io/certificates
   <br>
3. Search for the subdomains with a certificate transparency tool for the domain name cryptohack.org
