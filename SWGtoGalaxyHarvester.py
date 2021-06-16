import utils.auth as auth
import utils.readscreen as rs
import utils.parsedata as par   
import json

login, gh_sid = auth.get_auth()
gh_sid = gh_sid.strip('\n')

getinfo = rs.get_resource_info()
resource_sample = rs.parse_validate_write(getinfo)
resource_sample.gh_sid = gh_sid
resource_sample.planet = "corellia"
resource_sample.forceOp = "verify"

sample_json = par.class_to_json(resource_sample)

# build string as form data
submit_string = '?'
test_dict = eval(sample_json)
for k,v in test_dict.items():
    submit_string = submit_string + k+"="+v+"&"

print(submit_string)


# r = auth.add_resource(login, submit_string)
# print(r.status_code)
# print(r.content)