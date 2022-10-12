using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyManager : MonoBehaviour
{
    public List<GameObject> enemy_list;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (GameManager.state == PlayState.Start)
        {
            for(int i=0; i < enemy_list.Count; i++)
            {
                enemy_list[i].SetActive(true);
            }
        }
    }
}
