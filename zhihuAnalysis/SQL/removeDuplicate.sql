insert into zhihu_users
select *,count(user_custom_url) from zhihu_temp group by user_custom_url