from threat_research import *



if __name__ == '__main__':
    value = "The attack is linked to the CoughingDown threat group, also known as TA428 TA428, as suggested by consistent service creation and C2 domain overlap. The CoughingDown Core Module was also identified. The use of the most recent malware iteration is attributed with medium confidence to a hacking group tracked as CoughingDown. EAGERBEE was initially identified by Elastic Security Labs, linked to a state-sponsored cyber-espionage group known as REF5961. It was observed in cyber-espionage attacks against Southeast Asian government agencies and linked to the Chinese nation-backed hacking collective, which Sophos tracked as “Crimson Palace.” Previous researchers had attributed EagerBee to Chinese threat group Iron Tiger (APT27), one of numerous groups that often collaborate with other China-backed state-sponsored actors. Western ISPs and telecommunications service providers (TSP) were heavily targeted by PRC-backed groups, including Salt Typhoon Salt Typhoon, who potentially obtained metadata associated with the communication habits of millions of the compromised providers’ customers metadata associated with communication habits. The new variant of EAGERBEE (aka Thumtais) Thumtais was observed in attacks by a Chinese state-aligned threat cluster tracked as Cluster Alpha Cluster Alpha, which overlaps with groups like BackdoorDiplomacy, REF5961, Worok, and TA428. BackdoorDiplomacy exhibits tactical similarities with another Chinese-speaking group codenamed CloudComputating (aka Faking Dragon) CloudComputating, attributed to a multi-plugin malware framework referred to as QSC QSC."
    text_output = f"#### \n {value} \n\n"
    # actors = get_actor(value)
    actors = ['Lazarus Group', 'Citrine Sleet', 'APT38', 'BlueNoroff', 'Stardust Chollima', 'Jade Sleet', 'UNC4899', 'Slow Pisces']
    if actors and 'None' not in actors:
        # threat_actors = eval(get_actor(value))
        # threat_actors = eval(actors)
        threat_actors = actors
        actor_name, links, context = pipeline(threat_actors, 'oneti', token)
        actor_info_name = ", ".join(f"{name}" for name in set(actor_name[:3]))
        # prof_links = "\n".join(f"- {link}" for link in set(links))
        valid_links = []

        for link in links:
            # Fetch the page content
            try:
                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                
                # Only include links with content exceeding 500 tokens
                if num_tokens > 500:
                    valid_links.append(link)
            except Exception as e:
                print(f"Error processing {link}: {e}")
        
        # Remove duplicates and format as a list
        prof_links = "\n".join(f"- {link}" for link in set(valid_links))    

        if context:
            context = context.replace('\n\n', '\n')
            if prof_links:
                text_output += f"- Based on MDTI profile for {actor_info_name} from the following links: \n\n{prof_links}\n\n The additional threat actor information is:\n\n {context}\n\n"
            else:
                text_output += f"- Based on profile for {actor_info_name} from the source and the related articles above: \n\n The additional threat actor information is:\n\n {context}\n\n"

    print("-"*100)
    print("Context: \n")
    print(context)
